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

client.run('ODkxODY4OTE5NzM5MDY0MzQz.YVEnqA.HhGUW2-7Z3tC6eVQmTDhV1MjbGs')
