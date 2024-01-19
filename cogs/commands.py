from discord.ext import commands
import requests
import logging
import logging.config


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add')
    async def add_place(self, ctx):
        """
        Function to pick
        """
        # placeholder
        await ctx.send(f"Added.")


logger = logging.getLogger('basic')

async def setup(bot):
    await bot.add_cog(Commands(bot))
