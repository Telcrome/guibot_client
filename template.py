from guibot.bot import GuiBot, Verbosity


async def main_routine(b: GuiBot):
    b.log('Starting the main function')
    answer = await b.send_command_by_json(
        {
            'cmd': 'Ping',  # Required field
            'to': 'debugconsole',
            'data': {}
        }
    )
    b.log(answer)

    b.log('Finished the main function')


if __name__ == '__main__':
    bot = GuiBot(
        channel_id="test",
        bot_id='python_script',
        web_address="ws://127.0.0.1:8080/ws",
        logic=main_routine,
        verbosity=Verbosity.File)
