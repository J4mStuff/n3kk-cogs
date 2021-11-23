from .pekofy import Pekofy
from redbot.core.bot import Red

def setup(bot: Red):
    cog = Pekofy()
    bot.add_cog(cog)