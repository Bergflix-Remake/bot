import discord


class ConfirmModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.Button("OK", self.close))
