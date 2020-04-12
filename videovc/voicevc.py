from redbot.core import commands

class VoiceVC(commands.Cog):
    """My custom cog"""

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def vc(self, ctx):
        """Generate a video chat url"""
        # Your code will go here
        if not message.author.bot:
            try:
                await ctx.send(ctx.guild.id)
                await ctx.send(ctx.author.voice.channel.id)
                await ctx.send("Here's your link: https:////discordapp.com\/channels//" + ctx.guild.id + "//" + ctx.author.voice.channel.id)
            except AttributeError:
                return await self._embed_msg(
                    ctx,
                    title=_("Unable To Generate Link"),
                    description=_("Connect to a voice channel first."),
                )