from redbot.core import commands
import discord


class Pekofy(commands.Cog):
    """Pekofy messages Peko!"""

    __author__ = "N3kk"
    __version__ = "0.1.0"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pekofy(self, ctx: commands.Context, text: str = None):
        """Pekofy the replied to message, previous message, or your own text."""
        #if not text:
        #    if hasattr(ctx.message, "reference") and ctx.message.reference:
        #        try:
        #            text = (
        #                await ctx.fetch_message(ctx.message.reference.message_id)
        #            ).content
        #        except (discord.Forbidden, discord.NotFound, discord.HTTPException):
        #            pass
        #    if not text:
        #        text = (await ctx.channel.history(limit=2).flatten())[
        #            1
        #        ].content or "I can't translate that!"
        #   text = self.pekofy(text)
        await ctx.send(text+"123")

    #@commands.command()
    #async def unpekofy(self, ctx: commands.Context, *, text: str = None):
    #    """Unpekofies the replied to message, previous message, or your own text."""
    #    if not text:
    #        if hasattr(ctx.message, "reference") and ctx.message.reference:
    #            try:
    #                text = (
    #                    await ctx.fetch_message(ctx.message.reference.message_id)
    #                ).content
    #            except (discord.Forbidden, discord.NotFound, discord.HTTPException):
    #                pass
    #        if not text:
    #            text = (await ctx.channel.history(limit=2).flatten())[
    #                1
    #            ].content or "I can't translate that!"
    #    await ctx.send(self.unpekofy(text))

    def pekofy(self, text: str):
        """Pekofy a text message"""

        sentences = text.split(".")

        for sentence in sentences:
            sentence += ", Peko"

        return text.join(".")

    def unpekofy():
        return "Not implemented, Peko!"
