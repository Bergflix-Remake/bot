import discord
from dotenv import load_dotenv
from os import getenv
import logging
from discord.ext import commands
from classes.rules import RulesView, RulesEmbed
from classes.welcome import WelcomeView, WelcomeEmbed
from classes.ask_question import AskView, AskEmbed
from classes.answer_querstion import AnswerView
from discord.commands import permissions

load_dotenv()

""" Logging """
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('[%(asctime)s][%(name)s/%(levelname)s] %(message)s'))
logger.addHandler(handler)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('[%(asctime)s][%(name)s/%(levelname)s] %(message)s'))
logger.addHandler(console)

""" Globals """
GUILD_IDS=[966345054509736036]

class BergflixBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("bf. "))
        self.persistent_views_added = False
    
    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(RulesView())
            self.add_view(AskView())
            self.persistent_views_added = True
        logging.info(f"Logged in as {self.user} (ID: {self.user.id})")

bot = BergflixBot()

""" Commands """

@bot.slash_command(guild_ids=GUILD_IDS)
async def ping(ctx):
    """ Pong! """
    await ctx.respond(f":ping_pong: Pong! {round(bot.latency * 1000)}ms")

@bot.slash_command(guild_ids=GUILD_IDS)
@permissions.is_owner()
async def rules(ctx: commands.Context):
    """ Send the rules in the current channel. May only be excuted by the server owner. """
    await ctx.defer(ephemeral=True)
    await ctx.send(embed=RulesEmbed(), view=RulesView())
    await ctx.respond(":ok_hand:", ephemeral=True)

@bot.slash_command(guild_ids=GUILD_IDS)
@permissions.is_owner()
async def welcome(ctx: commands.Context):
    """ Send the welcome message in the current channel. May only be excuted by the server owner. """
    await ctx.defer(ephemeral=True)
    await ctx.send(embed=WelcomeEmbed, view=WelcomeView())
    await ctx.respond(":ok_hand:", ephemeral=True)

@bot.slash_command(guild_ids=GUILD_IDS)
@permissions.is_owner()
async def ask_embed(ctx: commands.Context):
    """ Send the ask message in the current channel. May only be excuted by the server owner. """
    await ctx.defer(ephemeral=True)
    await ctx.send(embed=AskEmbed(), view=AskView())
    await ctx.respond(":ok_hand:", ephemeral=True)

@bot.slash_command(guild_ids=GUILD_IDS)
@permissions.has_role("Team")
async def answer(ctx: commands.Context, question: str, answer: str):
    """Answer a question via command."""
    await ctx.defer(ephemeral=True)
    channel = discord.utils.get(ctx.guild.channels, name="💬faq")
    embed = discord.Embed(title=question, color=discord.Color.blue(), description=answer)
    await channel.send(embed=embed)
    await ctx.respond(":ok_hand:", ephemeral=True)

bot.run(getenv("TOKEN"))