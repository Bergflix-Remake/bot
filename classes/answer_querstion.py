import discord


class AnswerModal(discord.ui.Modal):
    def __init__(self, question):
        super().__init__(title="Antworten")
        self.add_item(discord.ui.InputText(
            label="Antwort", value="Antwort hier eingeben...", style=discord.InputTextStyle.long))
        self.question = question

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        # Get the channel named "💬faq"
        channel = discord.utils.get(interaction.guild.channels, name="💬faq")
        embed = discord.Embed(title=self.question, color=discord.Color.blue(
        ), description=self.children[0].value)
        await channel.send(embed=embed)
        await interaction.followup.send(embed=discord.Embed(title="Antwort wurde gesendet", color=discord.Color.green()), ephemeral=True)


class AnswerView(discord.ui.View):
    def __init__(self, question):
        super().__init__(timeout=None)
        self.question = question

    @discord.ui.button(label="Antworten", emoji="💬", style=discord.ButtonStyle.primary)
    async def answer(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(AnswerModal(self.question))
