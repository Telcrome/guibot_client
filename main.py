import itertools
import asyncio
import websockets as ws
import time
import json

LOCAL_ADDRESS = '127.0.0.1'
PORT = 5678
LOCAL_URI = f'ws://{LOCAL_ADDRESS}:{PORT}/ws'
USER_NAME = 'bot_script'


async def logic(websocket):
    # document.querySelector('input[aria-label="Description, "]').value = '1'
    test_command = {
        'cmd': 'setText',
        'selector': 'input[aria-label="Description, "]',
        'value': 'some text for the query'
    }
    await websocket.send(json.dumps(test_command))
    await asyncio.sleep(10)


async def main():
    # uri = LOCAL_URI
    # websocket = ws.connect(LOCAL_URI)
    # await websocket.send('test')

    async with ws.connect(LOCAL_URI) as websocket:
        await websocket.send(json.dumps({
            'user': USER_NAME,
            'type': 'master'
        }))

        await logic(websocket)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
