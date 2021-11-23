"""Bot"""
from redbot.core.bot import Red
from .pekofy import Pekofy

def setup(bot: Red):
    """Bot"""
    cog = Pekofy()
    bot.add_cog(cog)
