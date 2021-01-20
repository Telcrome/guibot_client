import sys
import typing as tau
import websockets as ws
import asyncio
import json
import logging

from enum import Enum

from guibot import REMOTE_WS


class Verbosity(Enum):
    Silent, File, Printer = range(3)


class GuiBot:

    def __init__(self,
                 channel_id: str,
                 logic: tau.Callable,
                 bot_id='python_script',
                 verbosity=Verbosity.File,
                 ws_address=""):
        self.channel_token = channel_id
        if not ws_address:
            ws_address = REMOTE_WS
        self.ws_address = ws_address
        self.logic = logic
        self.websocket = None
        self.bot_id, self.verbosity = bot_id, verbosity

        if self.verbosity == Verbosity.File:
            logging.basicConfig(filename='bot.log', level=logging.INFO)

        # Starting the logic
        self.start_bot()

    def log(self, c: tau.Any, f=logging.info) -> None:
        if self.verbosity == Verbosity.File:
            f(str(c))
        elif self.verbosity == Verbosity.Printer:
            print(c)

    async def send_command(self, command: tau.Dict):
        await self.websocket.send(json.dumps(command))
        answer = await self.websocket.recv()
        return json.loads(answer)

    async def main(self):

        async with ws.connect(self.ws_address) as websocket:
            self.websocket = websocket
            await websocket.send(json.dumps({
                'channel': self.channel_token,
                'id': self.bot_id,
                'cmds': [],
                'protection': 'ip'
            }))

            # The server sends a message when the client logged in
            login_answer = json.loads(await self.websocket.recv())
            assert login_answer['message_type'] != 'error'

            await self.logic(self)

    def start_bot(self):
        asyncio.get_event_loop().run_until_complete(self.main())
