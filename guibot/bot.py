import sys
import typing as tau
import websockets as ws
import asyncio
import json
import logging

from enum import Enum


class Verbosity(Enum):
    Silent, File, Printer = range(3)


class GuiBot:

    def __init__(self,
                 channel_id: str,
                 web_address: str,
                 logic: tau.Callable,
                 bot_id='python_script',
                 verbosity=Verbosity.File):
        self.channel_token = channel_id
        self.web_address = web_address
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

    async def send_command_by_json(self, command: tau.Dict):
        await self.websocket.send(json.dumps(command))
        answer = await self.websocket.recv()
        return json.loads(answer)

    async def main(self):
        # uri = LOCAL_URI
        # self.websocket = ws.connect(LOCAL_URI)
        # await websocket.send('test')

        async with ws.connect(self.web_address) as websocket:
            self.websocket = websocket
            await websocket.send(json.dumps({
                'channel': self.channel_token,
                'id': self.bot_id,
                'cmds': [],
                'protection': 'ip'
            }))
            answer = await self.websocket.recv()

            await self.logic(self)

    def start_bot(self):
        asyncio.get_event_loop().run_until_complete(self.main())
