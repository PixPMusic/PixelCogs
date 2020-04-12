from .voicevc import VoiceVC

async def setup(bot):
    bot.add_cog(VoiceVC())