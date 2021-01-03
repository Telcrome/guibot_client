from pprint import pprint
import itertools
import asyncio
import time
from guibot.bot import GuiBot
import pyautogui

LOCAL_ADDRESS = '127.0.0.1'
PORT = 5678
LOCAL_URI = f'ws://{LOCAL_ADDRESS}:{PORT}/ws'
USER_NAME = 'bot_script'

bc_textbox_test = {
    'cmd': 'setText',
    'selector': 'input[aria-label="Description, "]',
    'value': 'some text for the query'
}
wiki_searchbar = {
    'cmd': 'setText',
    'selector': '#searchInput',
    'value': 'hallo papa'
}
wait_for = {
    'cmd': 'waitForElement',
    'selector': 'input[aria-label="Description, "]'
}
test_click = {
    'cmd': 'clickElement',
    'selector': '#js-lang-list-button'
}


async def logic(h: GuiBot):
    # answer = await h.send_command_by_json(wait_for)
    # pprint(answer)

    while True:

        answer = await h.send_command_by_json(test_click)
        pprint(answer)

        print('sleeping for 5 seconds')
        await asyncio.sleep(3)
        #
        # answer = await h.send_command_by_json(test_click)
        # pprint(answer)


if __name__ == '__main__':
    bot = GuiBot(USER_NAME, LOCAL_URI, logic)
    bot.start_bot()
