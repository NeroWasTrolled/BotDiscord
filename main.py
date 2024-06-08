import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Modal, Select, TextInput, View

id_do_servidor = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')
    await bot.tree.sync(guild=discord.Object(id=id_do_servidor))


class CharacterRegistrationModal(Modal):

    def __init__(self):
        super().__init__(title="Registrar Personagem")

        self.add_item(
            TextInput(label="Nome do Personagem",
                      placeholder="Digite o nome do personagem aqui...",
                      max_length=100))

        self.select = Select(placeholder="Selecione a classe do personagem...",
                             options=[
                                 discord.SelectOption(label="Saber",
                                                      value="Saber"),
                                 discord.SelectOption(label="Ranger",
                                                      value="Ranger"),
                                 discord.SelectOption(label="Lancer",
                                                      value="Lancer"),
                                 discord.SelectOption(label="Fighter",
                                                      value="Fighter"),
                                 discord.SelectOption(label="Mage",
                                                      value="Mage"),
                                 discord.SelectOption(label="Summoner",
                                                      value="Summoner"),
                                 discord.SelectOption(label="Assassin",
                                                      value="Assassin"),
                                 discord.SelectOption(label="Berserk",
                                                      value="Berserk"),
                             ],
                             min_values=1,
                             max_values=1)
        self.add_item(self.select)

    async def on_submit(self, interaction: discord.Interaction):
        character_name = self.children[0].value
        character_class = self.select.values[0]

        print(f"Character Name: {character_name}")
        print(f"Character Class: {character_class}")

        embed = discord.Embed(
            title="Personagem Registrado",
            description=
            f"O personagem **{character_name}** da classe **{character_class}** foi registrado com sucesso!",
            color=discord.Color.green())
        await interaction.response.send_message(embed=embed)

        print("Modal enviado com sucesso!")


@bot.tree.command(guild=discord.Object(id=id_do_servidor),
                  name='registro',
                  description='Registrar um novo personagem')
async def registro(interaction: discord.Interaction):
    modal = CharacterRegistrationModal()
    await interaction.response.send_modal(modal)


bot.run("")
