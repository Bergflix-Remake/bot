from discord.ui import Button
from discord import Embed
import discord


WelcomeEmbed = Embed.from_dict(
    {
        "title": "Willkommen bei Bergflix. 👋",
        "color": 15994682,
        "description": "Willkommen auf dem offiziellen Discord Server von Bergflix!\nBitte lies dir als Erstes die <#966345055038230590> durch, und sieh dir gerne das <#966345055038230592> an.\nUnten findest du wichtige links.\n~ Dein Bergflix. Remake-Team",
        "timestamp": "",
        "url": "https://bergflix.de/",
        "author": {
            "name": "Bergflix Remake",
            "url": "https://github.com/bergflix-remake",
            "icon_url": "https://cdn.bergflix.de/logo/light.png"
        },
        "image": {
            "url": "https://cdn.bergflix.de/logo/long_light.png"
        },
        "thumbnail": {},
        "footer": {},
        "fields": []
    })

class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        website_button = Button(label="Website", emoji="🌐", url="https://bergflix.de/")
        github_button = Button(label="GitHub", emoji="💻", url="https://github.com/bergflix-remake")
        developement_button = Button(label="Developement-Seite (falls verfügbar)", emoji="🚧", url="https://dev.bergflix.de/")
        for i in [website_button, github_button, developement_button]:
            self.add_item(i)

    

