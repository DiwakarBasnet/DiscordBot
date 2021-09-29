import discord


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 892390146828296192

    async def on_ready(self):
        print('Online')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on a reaction emoji
        """
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Aalu')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Shit Heads')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Monke')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on emoji removed
        """
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Aalu')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Shit Heads')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Monke')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('Bot Token')
