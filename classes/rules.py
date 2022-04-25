from asyncio.log import logger
from datetime import datetime
import discord
from discord.ext import commands
from classes.design import Images, Colors


class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    class SuccessEmbed(discord.Embed):
        def __init__(self):
            super().__init__(
                title="Rules accepted",
                description="You are now a member of the community!",
                color=discord.Color.green(),
            )

    @discord.ui.button(
        label="Accept",
        style=discord.ButtonStyle.green,
        custom_id="rules:accept",
        emoji="✅",
    )
    async def accept(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        role = discord.utils.get(
            interaction.guild.roles, name="Communitymitglied")
        await interaction.user.add_roles(role)
        await interaction.followup.send(embed=self.SuccessEmbed(), ephemeral=True)
        logger.info(f"{interaction.user} accepted the rules")
        logger.debug(f"Interaction: {interaction}")


class RulesEmbed(discord.Embed):
    def __init__(self):
        super().__init__(
            title="Regeln",
            description="""
                - Sei nett und respektvoll zu anderen.
                - Teile keinen unangemessenen Inhalt.
                - Spamme nicht in einem der Server-Kanäle.
                - Benutze angemessene Discord-Namen und Avatare.
                - Vermeide es, über kontroverse Themen wie Religion oder Politik zu sprechen oder solche Inhalte zu teilen.
                - Es ist verboten, Gespräche in Sprachkanälen ohne ausdrückliche erlaubniss von allen beteiligten aufzuzeichnen.
                - Respektiere das Thema jedes Kanals.
                - Jegliche Benutzung diskriminierender Sprache und Hassrede ist verboten.
                - Das unerlaubte Verteilen von nicht lizenziertem Material ist verboten.
                - Es ist verboten, die persönlichen Informationen anderer zu veröffentlichen.
                - Wir tolerieren keine Art von Mobbing, Belästigung, Bedrohung, Trollen, Erpressung oder unangemessenen DMs.
                - Sende keine bösartigen oder schädlichen Links oder Dateien.
                - Mitglieder müssen 13+ sein, um diesen Discord-Server verwenden zu können.
                - Bitte folge den Discord-Nutzungsbedingungen und allen Anweisungen der Mitarbeiter jederzeit.
                - Wir fördern Vielfalt, Inklusion und freie Meinungsäußerung für alle. Daher erwarten wir von unseren Mitgliedern, dass ihre Interaktionen respektvoll und von diesen Grundsätzen geprägt sind.
                - Diese Regeln können sich jederzeit ändern. Es ist daher wichtig, sie regelmäßig zu überprüfen.
                - Moderatoren behalten sich das Recht vor, Nutzer nach eigenem Ermessen zu warnen und zu sperren.
            """,
            color=Colors["primary"],
            timestamp=datetime.now(),
        )
        self.set_thumbnail(url=Images["light"])
        self.set_footer(
            text="Diese Regeln können sich jederzeit ändern. Letztes Update", icon_url=Images["light_bg"])
