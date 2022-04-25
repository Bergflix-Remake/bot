import discord
from classes.answer_querstion import AnswerView


class AskModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Frage Stellen")
        self.add_item(discord.ui.InputText(label="Frage", value="Frage hier eingeben...", style=discord.InputTextStyle.long))
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        # Get the channel named "questions"
        channel = discord.utils.get(interaction.guild.channels, name="questions")
        embed = discord.Embed(title="Frage von {}".format(
            interaction.user.name), color=discord.Color.blue(), description=self.children[0].value)
        await channel.send(embed=embed, view=AnswerView(self.children[0].value))
        await interaction.followup.send(embed=discord.Embed(title="Frage wurde gesendet", color=discord.Color.green()), ephemeral=True)

class AskView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Frage stellen", emoji="💬", style=discord.ButtonStyle.primary, custom_id="ask:ask")
    async def ask(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(AskModal())

class AskEmbed(discord.Embed):
    def __init__(self):
        super().__init__(title="Fragen", color=discord.Color.blue())
        self.add_field(name="Frage stellen", value="Mit diesem Button kannst du eine Frage stellen, die nach dem Beantworten durchs Team auf dem Server angezeigt wird.")