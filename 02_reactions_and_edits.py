import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')
    if message.content == 'nerd':
        await message.add_reaction('\U0001F913')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'PUSSY ALERT!!!  '
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}\n'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

client.run('Bot Token')
