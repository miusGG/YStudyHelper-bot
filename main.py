import discord
from discord.ext import commands
from info import token
from discord.utils import get
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
auth_channel1 = 1206656465616764998
guild_id = 1206656352857096312


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def question(ctx):
    user = ctx.message.author
    guild = ctx.guild
    member = user
    message_content = f'Канал для вопроса учителю создан - тезисно напиши там свой вопрос. Чтобы удалить канал - >delete_channel'
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'Вопрос от {member}', overwrites=overwrites)
    await ctx.message.delete()




class HelperView(discord.ui.View):
    @discord.ui.button(label="Как задать вопрос учителю?", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, interaction, button):
        await interaction.response.send_message("В специальном тексковом канале пишите команду - >question")

    @discord.ui.button(label="Все команды", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button):
        await interaction.response.send_message("Вот все доступные команды:\n>question - создать канал для вопроса учителю.\n>? - команда по выдачи документаций и полезных материалов для учеников!")


@bot.event
async def on_member_join(member):
    role = member.guild.get_role(role_id=1208730162414485555)
    await member.add_roles(role)


@bot.command()
async def make_channel(ctx):
    user = ctx.author
    guild = ctx.guild
    member = user
    message_content = f'Канал для аунтификации пользователя - "{member}" успешно создан! Выберите ваш ГОД и ГРУППУ обучния в соответсвующем канале.'
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'auth for {member}', overwrites=overwrites)
    await ctx.message.delete()

    name_msg = member

    message1 = await channel.send('Выберите группу и год:\n1. Группа 1\n2. Группа 2')

    await message1.add_reaction('1️⃣')
    await message1.add_reaction('2️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        role1 = discord.utils.get(ctx.guild.roles, name='группа 1')
    elif reaction.emoji == '2️⃣':
        role1 = discord.utils.get(ctx.guild.roles, name='группа 2')
    else:
        await message1.delete()
        await channel.send('Неверный выбор.')
        return

    await message1.delete()
    await channel.send('Выбор учтен.')

    message = await channel.send('Выберите год:\n1. Год 1\n2. Год 2')

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

    await message.delete()
    await channel.send('Выбор учтен.')

    global auth_channel1

    guild = bot.get_guild(guild_id)
    auth_channel = guild.get_channel(auth_channel1)

    check_mesaage = await auth_channel.send(f'Подтвердите действия {name_msg} - Он выбрал str(его группа и год)')
    await check_mesaage.add_reaction('✅')
    await check_mesaage.add_reaction('❌')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['✅', '❌']

    try:
        reaction, _ = await bot.wait_for('reaction_add', timeout=None, check=check)
        if str(reaction.emoji) == '✅':
            await auth_channel.send("ОДОБРЕНО!")

            await user.send("ВАША ЗАЯВКА ОДОБРЕНА")

            await ctx.author.add_roles(role)
            await ctx.author.add_roles(role1)
            await channel.send('Выбор подтвержден.')
            await channel.delete()
        elif str(reaction.emoji) == '❌':
            await auth_channel.send("НЕОДОБРЕНО!")

            await user.send("ВАША ЗАЯВКА НЕ ОДОБРЕНА")

            await channel.send('Выбор не поддтвержден')
            await channel.delete()
    except asyncio.TimeoutError:
        await ctx.send("You did not react in time.")



@bot.command()
async def delete_channel(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ['да', 'нет']

    await ctx.send('Вы уверены, что хотите удалить этот чат? Напиши - (да/нет)')
    confirmation = await bot.wait_for('message', check=check)

    if confirmation.content.lower() == 'да':
        await ctx.channel.delete()
        await ctx.send('Чат успешно удален.')
    else:
        await ctx.send('Удаление чата отменено.')


@bot.command()
async def helper(ctx):
    await ctx.message.delete()
    user = ctx.message.author
    member = ctx.author
    message_content = f'Руководство по использованию этого бота.\nВот все доступные команды:\n>question - создать канал для вопроса учителю.\n>? - команда по выдачи документаций и полезных материалов для учеников!\nВыберите что бы Вы хотели бы узнать:'
    await user.send(message_content, view=HelperView())


bot.run(token)
