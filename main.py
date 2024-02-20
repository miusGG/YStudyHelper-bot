import discord  # Подключаем библиотеку
from discord.ext import commands
from info import token
from discord.utils import get
import asyncio

intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def question(ctx):
    await ctx.send('pong')


class HelperView(discord.ui.View):
    @discord.ui.button(label="Как задать вопрос учителю?", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, interaction, button):
        await interaction.response.send_message("В специальном тексковом канале пишите команду - >question")

    @discord.ui.button(label="Все команды", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button):
        await interaction.response.send_message("Commands")


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="new")
    await member.add_roles(role)


@bot.command()
async def make_channel(ctx):
    await ctx.message.delete()
    user = ctx.message.author
    guild = ctx.guild
    member = ctx.author
    message_content = f'Канал для аунтификации пользователя - "{member}" успешно создан! Выберите ваш ГОД и ГРУППУ обучния.'
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'auth for {member}', overwrites=overwrites)

    message = await channel.send('Выберите группу и год:\n1. Группа 1\n2. Группа 2')

    # Добавляем реакции к сообщению
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        role = discord.utils.get(ctx.guild.roles, name='группа 1')
    elif reaction.emoji == '2️⃣':
        role = discord.utils.get(ctx.guild.roles, name='группа 2')
    else:
        await message.delete()
        await channel.send('Неверный выбор.')
        return
    await ctx.author.add_roles(role)
    await message.delete()
    await channel.send('Выбор подтвержден.')

    message = await channel.send('Выберите год:\n1. Год 1\n2. Год 2')

    # Добавляем реакции к сообщению
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        role = discord.utils.get(ctx.guild.roles, name='год 1')
    elif reaction.emoji == '2️⃣':
        role = discord.utils.get(ctx.guild.roles, name='год 2')
    else:
        await message.delete()
        await channel.send('Неверный выбор.')
        return
    await ctx.author.add_roles(role)
    await message.delete()
    await channel.send('Выбор подтвержден.')

    await channel.delete()


@bot.command()
async def delete_channel(ctx, channel_id):
    channel = bot.get_channel(int(channel_id))
    await channel.delete()
    await ctx.send("Канал удален")


@bot.command()
async def helper(ctx):
    await ctx.message.delete()
    user = ctx.message.author
    member = ctx.author
    message_content = f'Руководство по использованию этого бота.\nВыберите что бы Вы хотели бы узнать:'
    await user.send(message_content, view=HelperView())


bot.run(token)
