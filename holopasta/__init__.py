"""Bot"""
from redbot.core.bot import Red
from .holopasta import Holopasta

def setup(bot: Red):
    """Bot"""
    cog = Holopasta(bot)
    bot.add_cog(cog)
