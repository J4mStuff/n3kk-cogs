"""Pekofy init script"""
from redbot.core.bot import Red
from .pekofy import Pekofy


def setup(bot: Red):
    """Setup"""
    cog = Pekofy(bot)
    bot.add_cog(cog)
