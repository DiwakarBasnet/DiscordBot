import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Bot online and ready to roll')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send("Hello World!!!")
    if message.content == 'Yo':
        await message.channel.send('Sup bitch')

client.run('Discord Token')
