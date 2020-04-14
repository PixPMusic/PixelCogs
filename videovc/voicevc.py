from redbot.core import commands

class VoiceVC(commands.Cog):
    """My custom cog"""

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def vc(self, ctx):
        """Generate a video chat url"""
        try:
            await ctx.send("Here's your link: https://discordapp.com/channels/" + str(ctx.guild.id) + "/" + str(ctx.author.voice.channel.id))
        except:
            await ctx.send("Connect to a voice channel first!")