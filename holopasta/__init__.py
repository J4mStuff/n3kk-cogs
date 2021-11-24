"""Holopasta init script"""
from redbot.core.bot import Red
from .holopasta import Holopasta


def setup(bot: Red):
    """Setup"""
    cog = Holopasta(bot)
    bot.add_cog(cog)
