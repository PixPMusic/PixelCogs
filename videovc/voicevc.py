from redbot.core import commands

class VoiceVC(commands.Cog):
    """My custom cog"""

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def vc(self, ctx):
        """Generate a video chat url"""
        try:
            await ctx.send("Here's your link: " + ctx.guild.id + " " + ctx.author.voice.channel.id)
        except AttributeError:
            return await self._embed_msg(
                ctx,
                title=_("Unable To Generate Link"),
                description=_("Connect to a voice channel first."),
            )