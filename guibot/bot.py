import sys
import typing as tau
import websockets as ws
import asyncio
import json


class GuiBot:

    def __init__(self, user_name: str, local_uri: str, logic: tau.Callable):
        self.user_name = user_name
        self.local_uri = local_uri
        self.logic = logic
        self.websocket = None

    async def send_command_by_json(self, command: tau.Dict):
        await self.websocket.send(json.dumps(command))
        answer = await self.websocket.recv()
        return json.loads(answer)

    async def main(self):
        # uri = LOCAL_URI
        # self.websocket = ws.connect(LOCAL_URI)
        # await websocket.send('test')

        async with ws.connect(self.local_uri) as websocket:
            self.websocket = websocket
            await websocket.send(json.dumps({
                'user': self.user_name,
                'type': 'master'
            }))

            await self.logic(self)

    def start_bot(self):
        asyncio.get_event_loop().run_until_complete(self.main())
