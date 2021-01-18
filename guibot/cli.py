import typing as tau
import click


@click.group()
def bot():
    """
    AI command line tools.
    """
    pass


@bot.command(name='test')
def trainer_reset_database():
    """
    Tests if the cli works
    """
    print('test')


if __name__ == '__main__':
    bot()
