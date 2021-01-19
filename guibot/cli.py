import os
import typing as tau
import click
import urllib.request

from guibot import REMOTE_HTTP


@click.group()
def bot():
    """
    AI command line tools.
    """
    pass


@bot.command(name='new')
@click.option('-f', '--filename', default='bot.py')
def bot_new(filename: str):
    """
    Tests if the cli works
    """
    url = rf"{REMOTE_HTTP}static/guibot-template.py"
    contents = urllib.request.urlopen(url).read()
    str_content: str = contents.decode('utf-8')
    # Strip weird newlines
    str_content = str_content.replace('\r', '')

    fullpath = os.path.join(os.getcwd(), filename)

    if os.path.exists(fullpath):
        print(f"Already exists: {fullpath} (doing nothing)")
    else:
        print(f"Creating {filename} at {os.getcwd()}")
        with open(fullpath, 'w+') as f:
            f.write(str_content)


if __name__ == '__main__':
    bot()
