from configparser import ConfigParser
import logging
import discord
from discord.ext import commands
import random, datetime
# TODO: Bot connecting to voice channel. Playing sounds in it.
# TODO: Playing sounds from web. (for example: youtube, vk, soundcloud?)

class Config:
    """
    Class for config and its' parsing.
    """
    def _init_(self):
        pass

    configparser = ConfigParser()

    def get_access_token(self):
        self.configparser.read('config.ini')
        access_token = self.configparser.get('Config', 'access_token')
        return access_token


logging.basicConfig(format=u'%(levelname)-9s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename='logs.log')

getconfig = Config()
TOKEN = getconfig.get_access_token()

client = commands.Bot(command_prefix='%')
client.remove_command('help')


def logging_message(ctx, command):
    """
    logging messages w/ commands into .log file
    TODO: decorator;
    """
    server = str(ctx.guild)
    chat = str(ctx.channel.name)
    username = str(ctx.author)
    logging.info(f'{server} | ({chat}) {username}: {command}')


def logging_response(ctx, response):
    """
    logging responses to commands into .log file
    TODO: combine w/ "logging_message"
    """
    username = str(ctx.author)
    logging.info(f'*Response sent to {username}: {response}')


@client.event
async def on_ready():
    print('Ready')
    logging.info('___We have been logged as a {0.user}___'.format(client))


@client.command()
async def help(ctx):
    """
    %help
    """
    command = r'%help'
    logging_message(ctx, command)

    embed = discord.Embed(
        title='Bot Commands',
        description='All available commands for today. \n ⠀',
        color= discord.Colour.green(),
    )

    embed.set_thumbnail(url='https://thiscatdoesnotexist.com/')     # Picture for %help command
    embed.add_field(
        name='%help',
        value='List of all commands. \n ⠀',
        inline=False
    )
    embed.add_field(
        # https://thiscatdoesnotexist.com/
        name='%cat',
        value="This cat doesn't exist. Doesn't work propely as for me. \n ⠀",
        inline=False
    )
    embed.add_field(
        # https://thisartworkdoesnotexist.com/
        name='%art',
        value="This art doesn't exist. Doesn't work propely as for me. \n ",
        inline=False
    )
    await ctx.send(embed=embed)

    logging_response(ctx, embed)


@client.command()
async def cat(ctx):
    """
    %cat
    TODO: find out how discord handle this website
    """
    command = r'%cat'
    logging_message(ctx, command)

    content = 'https://thiscatdoesnotexist.com/'
    await ctx.send(content=content)

    logging_response(ctx, content)


@client.command()
async def art(ctx):
    """
    %art
    TODO: find out how discord handle this website
    """
    command = r'%art'
    logging_message(ctx, command)

    content = 'https://thisartworkdoesnotexist.com/'
    await ctx.send(content=content)

    logging_response(ctx, content)


if __name__ == '__main__':
    logging.info('__LAUNCHING MAIN PROGRAM___')
    client.run(TOKEN)


# ______________________JUNKYARD______________________
#     if user_message.lower() == 'hello':
#         response = f'Hello {username} !'
#         await message.channel.send(response)
#         logging.info(f'*Response sent :{ {response} }')
#         return
#
#     elif user_message.lower() == 'bye':
#         response = f'{username} is out.'
#         await message.channel.send(response)
#         logging.info(f'*Response sent : {response}')
#         return
#
#     if str(message.channel) == 'talking-machine':            # checking for channel name
#         print('MESSAGE IN SPECIAL CHANNEL')
#     else:
#         pass
#
#
#
# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#
#     if message.author == client.user:           # logging, checks for bot's name
#         pass
#     else:
#         logging.info(f'{username}: {user_message} ({channel})')
#
#
#
# def logging_message(ctx):
#     """
#     Special decorator for logging messages with commands
#     """
#     def my_decorator(func):
#         @client.event
#         def on_command(message):
#             username = str(message.author).split('#')[0]
#             user_message = ' ' # str(message.content)
#             channel = str(message.channel.name)
#
#             func()
#
#             if message.author == client.user:           # logging, checks for bot's name
#                 pass
#             else:
#                 logging.info(f'{username}: {user_message} ({channel})')
#
#             return func()
#         return on_command
#     return logging_message
#
#
# @logging_message()