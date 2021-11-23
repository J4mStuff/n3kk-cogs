from .pekofy import Pekofy


def setup(bot):
    bot.add_cog(Pekofy(bot))