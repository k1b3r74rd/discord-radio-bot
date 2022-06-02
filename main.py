from configparser import ConfigParser
import logging
import discord
from discord.ext import commands

# TODO: sounds from youtube || vk || soundcloud
# TODO: start involving radio.garden


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


# Logging information into logs.log file
# TODO: cleaner log file
logging.basicConfig(format=u'%(levelname)-9s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename='logs.log')

# Getting personal information from config.ini
getconfig = Config()
TOKEN = getconfig.get_access_token()

# Preparing API and settings for commands for bot
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
        name='%botping',
        value="Checks bot ping \n ⠀",
        inline=False
    )
    embed.add_field(
        # https://thiscatdoesnotexist.com/
        name='%cat',
        value="This cat doesn't exist. Doesn't work propely as for me. \n",
        inline=False
    )
    embed.add_field(
        # https://thisartworkdoesnotexist.com/
        name='%art',
        value="This art doesn't exist. Doesn't work propely as for me. \n ⠀",
        inline=False
    )
    embed.add_field(
        name='%join',
        value="Voice command. Joins to voice channel. \n ",
        inline=False
    )
    embed.add_field(
        name='%perfect',
        value="Voice command. Plays 'Perfect' quote from Quake 3 Arena. \n ",
        inline=False
    )
    embed.add_field(
        name='%perfect',
        value="Voice command. Plays 'Fresh meat' quote from DOTA 2. \n ",
        inline=False
    )
    embed.add_field(
        name='%disconnect',
        value="Voice command. Disconnects from voice channel. \n ⠀",
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


@client.command()
async def botping(ctx):
    """
    %botping
    """
    command = r'%botping'
    logging_message(ctx, command)

    ping_raw = client.latency
    ping = round(ping_raw * 1000)
    content = f'My ping is {ping}ms'
    await ctx.send(content)

    logging_response(ctx, content)


@client.command(pass_context = True)
async def join(ctx):
    """
    %join - joins voice channel to summoner
    """
    command = r'%join'
    logging_message(ctx, command)

    if ctx.author.voice:
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
        await ctx.send(r'Joined.')
    else:
        await ctx.send(r'You are not in a voice channel to use this command.')

    logging_response(ctx, r'Reply sent.') # TODO: fix message and response sending


@client.command(pass_context = True)
async def disconnect(ctx):
    """
    %disconnect - leaves voice channel
    """
    command = r'%disconnect'
    logging_message(ctx, command)

    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send(r'Disconnected.')
    else:
        await ctx.send(r'Not in a voice channel.')

    logging_response(ctx, 'Reply sent') # TODO: fix message and response sending


@client.command(pass_context = True)
async def perfect(ctx):
    """
    %perfect - plays "perfect" quote from Quake 3 Arena. WAV file on PC.
    """
    command = r'%perfect'
    logging_message(ctx, command)

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    source = r'perfect.wav'
    audio_source = discord.FFmpegPCMAudio(source)

    if not voice_client.is_playing():  # TODO: queue?
        voice_client.play(audio_source, after=None)
        await ctx.send('Perfect.')

    logging_response(ctx, 'Sound involved: Perfect.')


@client.command(pass_context = True)
async def freshmeat(ctx):
    """
    %freshmeat - plays "fresh meat" quote from DOTA 2. MP3 file on website.
    """
    command = r'%freshmeat'
    logging_message(ctx, command)

    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

    source = r"https://static.wikia.nocookie.net/dota2_ru_gamepedia/images/4/48/Pud_ability_devour_02_ru.mp3/revision" \
             r"/latest?cb=20170413110428 "
    audio_source = discord.FFmpegPCMAudio(source=source)

    if not voice_client.is_playing():  # TODO: queue?
        voice_client.play(audio_source, after=None)
        await ctx.send('Fresh meat.')

    logging_response(ctx, 'Sound involved: Fresh meat.')


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