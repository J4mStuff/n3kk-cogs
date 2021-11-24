from discord import message
from redbot.core import commands
import re
import discord


class Pekofy(commands.Cog):
    #"""Pekofy messages Peko!"""

    __author__ = "N3kk"
    __version__ = "1.1.2"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pekofy(self, ctx: commands.Context, *, text: str = None):
        """This does stuff!"""

        text_block = await self.get_text(ctx, text)
        message = await self.pekofy_text(text_block)

        await ctx.send(message)

    @commands.command()
    async def unpekofy(self, ctx: commands.Context, *, text: str = None):
        text_block = await self.get_text(ctx, text)
        message = await self.unpekofy_text(text_block)

        await ctx.send(message)

    async def pekofy_text(self, text: str = None):
        signs = {
            r'(?<!peko)(\.+)': ", peko\\1",
            r'(?<!peko)([\?|\!]+)': ", PEKO?!?",
            r'(?<!peko)([^\!]|\s|$)(\?+)([^\!]|\s|$)': "\\1, PEKO\\2\\3",
            r'(?<!peko)(\?+[^\!\?])': ", p-peko\\1",
            r'(?<!peko)(\~+)': ", peko\\1",
            r'(?<!peko)([^\?|\.\!]+)$': "\\1, peko."
        }
        for key, value in signs.items():
            text = re.sub(key, value, text, 0, re.IGNORECASE)
        return text

    async def unpekofy_text(self, text: str = None):
        signs = [r',\s*peko(\.)', r',\s*peko(\!)', r',\s*peko(\?)']
        for sign in signs:
            text = re.sub(sign, "\\1", text, 0, re.IGNORECASE)
        return text

    async def get_text(self, ctx: commands.Context, text: str = None):
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
        return text
