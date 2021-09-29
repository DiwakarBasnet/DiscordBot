from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command()
async def punch(ctx, arg):
    """
    !punch Bob
    """
    await ctx.send(f'Punched {arg}')


@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Bob Bobby
    """
    await ctx.send(f'Punched {arg1} and {arg2}')


@bot.command()
async def roundhouse_kick(ctx, *arg):
    """
    !roundhouse_kick Bob Bobby Poopypants Borat
    """
    everyone = ', '.join(arg)
    await ctx.send(f'Roundhouse kicked {everyone}')


@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed)
    !info
    """
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

bot.run('Bot token')
