import disnake
from disnake.ext import commands
from disnake import TextInputStyle


bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())



# Subclassing the modal.
class MyModal(disnake.ui.Modal):
    def __init__(self):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Name",
                placeholder="Please enter your preferred full name",
                custom_id="name",
                style=TextInputStyle.short,
                max_length=32,
            ),
        ]
        super().__init__(title="Verification", components=components)

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        user = inter.author
        name = inter.text_values["name"]
        wugs = bot.get_guild(695789035494572042).get_role(961424365705105409)
        await user.edit(nick=name, roles=[wugs])
        await inter.response.send_message("Welcome to the server!", ephemeral=True)




@bot.listen("on_button_click")
async def cool_button_listener(inter: disnake.MessageInteraction):
    if inter.component.custom_id != "cool_button":
        # Since `inter.component` returns the component that triggered the interaction,
        # this is used to filter interactions for components other than the button we wish to
        # process with this listener.
        return

    # Thus, we end up with only buttons sent by the `send_button` command,
    # since those buttons were sent with `custom_id=cool_button`.
    # At this point, this listener is practically identical to the callback of a view button.
    await inter.response.send_modal(modal=MyModal())


@bot.command()
async def send_button(ctx: commands.Context):
    await ctx.send(
        "Welcome to the SLUgS Discord Server! To gain access, click the button below.",
        components=disnake.ui.Button(label="Begin Verification", custom_id="cool_button", style=disnake.ButtonStyle.blurple),
    )


bot.run("MTE0MzkxNDI5NjI2MzMyMzc5MA.GFToSF.MTw5I66okTDsc9M7pmx_3MohVEMXexMfD3phmE")

