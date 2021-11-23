from redbot.core import commands
import discord

class Pekofy(commands.Cog):
    #"""Pekofy messages Peko!"""

    __author__ = "N3kk"
    __version__ = "0.1.0"

    def __init__(self, bot):
        self.bot = bot

    async def pekofy(self, text: str):
        """Pekofy a text message"""

        sentences = text.split(".")

        for sentence in sentences:
            sentence += ", Peko"

        result = text.join(".")

        return result

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!") 

    @commands.command()
    async def pekofy(self, ctx: commands.Context, *, text: str = None):
        """This does stuff!"""
        text_block = await self.get_text(ctx, text)

        sentences = text_block.split(".")
        message = ""
        for sentence in sentences:
        	if(sentence is not ""):
        		message = message + sentence + ", Peko."

        await ctx.send(message)


    @commands.command()
    async def unpekofy(self, ctx: commands.Context, *, text: str = None):
        await ctx.send("Not implemented, Peko!")

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