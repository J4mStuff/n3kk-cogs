"""Main pekofication script"""
import re
import discord
from redbot.core import commands


class Pekofy(commands.Cog):
    """Pekofy messages Peko!"""

    __author__ = "N3kk"
    __version__ = "1.1.2"

    def __init__(self, bot):
        self.bot = bot
        self.message_text = ""

    @commands.command()
    async def pekofy(self, ctx: commands.Context, *, text: str = None):
        """Pekofication command"""

        await self.get_text(ctx, text)
        await self.pekofy_text()
        await ctx.send(self.message_text)

    @commands.command()
    async def unpekofy(self, ctx: commands.Context, *, text: str = None):
        """Unpekofication command"""

        await self.get_text(ctx, text)
        await self.unpekofy_text()
        await ctx.send(self.message_text)

    async def pekofy_text(self):
        """Actual pekofication functionality"""

        regex_hash = {
            r'(?<!peko)(\.+)': ", peko\\1",
            r'(?<!peko)([\?|\!]+)': ", PEKO?!?",
            r'(?<!peko)([^\!]|\s|$)(\?+)([^\!]|\s|$)': "\\1, PEKO\\2\\3",
            r'(?<!peko)(\?+[^\!\?])': ", p-peko\\1",
            r'(?<!peko)(\~+)': ", peko\\1",
            r'(?<!peko)([^\?|\.\!]+)$': "\\1, peko."
        }

        for key, value in regex_hash.items():
            self.message_text = re.sub(
                key, value, self.message_text, 0, re.IGNORECASE)

    async def unpekofy_text(self):
        """Actual unpekofication functionality"""

        regex = [r',\s*peko(\.)', r',\s*peko(\!)', r',\s*peko(\?)']
        for reg in regex:
            self.message_text = re.sub(
                reg, "\\1", self.message_text, 0, re.IGNORECASE)

    async def get_text(self, ctx: commands.Context, text: str = None):
        """Get text from command arguments
        /.pekofy [text]/
        if unavailable get message which command replied to
        if unavailable get previous message
        """

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

        self.message_text = text
