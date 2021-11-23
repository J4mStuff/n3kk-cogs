from redbot.core import commands
import discord
from redbot.core.utils import common_filters
import asyncio

class Pekofy(commands.Cog):
    """Pekofy messages Peko!"""

    __author__ = "N3kk"
    __version__ = "0.1.0"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command(aliases=["owo"])
    async def pekofy(self, ctx: commands.Context, *, text: str = None):
        """Uwuize the replied to message, previous message, or your own text."""
        if not text:
            if hasattr(ctx.message, "reference") and ctx.message.reference:
                try:
                    text = (
                        await ctx.fetch_message(ctx.message.reference.message_id)
                    ).content
                except (discord.Forbidden, discord.NotFound, discord.HTTPException):
                    pass
            if not text:
                text = (await ctx.channel.history(limit=2).flatten())[
                    1
                ].content or "I can't translate that!"
        await self.type_message(
            ctx.channel,
            self.pekofy(text),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False
            ),
        )

    @commands.command()
    async def pekofy2(self, ctx, text: str = None):
        """Pekofy the replied to message, previous message, or your own text."""
        if not text:
            if hasattr(ctx.message, "reference") and ctx.message.reference:
                try:
                    text = (
                        await ctx.fetch_message(ctx.message.reference.message_id)
                    ).content
                except (discord.Forbidden, discord.NotFound, discord.HTTPException):
                    pass
            if not text:
                text = (await ctx.channel.history(limit=2).flatten())[
                    1
                ].content or "I can't translate that!"
        await ctx.send(self.pekofy(text))

    async def type_message(
        destination: discord.abc.Messageable, content: str, **kwargs
    ) -> discord.Message:
        """Simulate typing and sending a message to a destination.
        Will send a typing indicator, wait a variable amount of time based on the length
        of the text (to simulate typing speed), then send the message.
        """
        content = common_filters.filter_urls(content)
        try:
            async with destination.typing():
                await asyncio.sleep(max(0.25, min(2.5, len(content) * 0.01)))
            return await destination.send(content=content, **kwargs)
        except discord.HTTPException:
            pass  # Not allowed to send messages to this destination (or, sending the message failed)

    def pekofy(self, text: str):
        """Pekofy a text message"""

        sentences = text.split(".")

        for sentence in sentences:
            sentence += ", Peko"

        return text.join(".")

    def unpekofy():
        return "Not implemented, Peko!"