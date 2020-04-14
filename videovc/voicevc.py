from redbot.core import commands
import datetime
import traceback
import aiohttp
import discord
from discord.embeds import EmptyEmbed
from discord.utils import escape_markdown as escape

from redbot.core.bot import Red

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
            await self._embed_msg(
                ctx,
                title=_("Unable To Generate Link"),
                description=_("Connect to a voice channel first."),
            )

    async def _embed_msg(self, ctx: commands.Context, **kwargs):
        colour = kwargs.get("colour") or kwargs.get("color") or await self.bot.get_embed_color(ctx)
        error = kwargs.get("error", False)
        success = kwargs.get("success", False)
        title = kwargs.get("title", EmptyEmbed) or EmptyEmbed
        _type = kwargs.get("type", "rich") or "rich"
        url = kwargs.get("url", EmptyEmbed) or EmptyEmbed
        description = kwargs.get("description", EmptyEmbed) or EmptyEmbed
        timestamp = kwargs.get("timestamp")
        footer = kwargs.get("footer")
        thumbnail = kwargs.get("thumbnail")
        contents = dict(title=title, type=_type, url=url, description=description)
        embed = kwargs.get("embed").to_dict() if hasattr(kwargs.get("embed"), "to_dict") else {}
        colour = embed.get("color") if embed.get("color") else colour
        contents.update(embed)
        if timestamp and isinstance(timestamp, datetime.datetime):
            contents["timestamp"] = timestamp
        embed = discord.Embed.from_dict(contents)
        embed.color = colour
        if footer:
            embed.set_footer(text=footer)
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        return await ctx.send(embed=embed)