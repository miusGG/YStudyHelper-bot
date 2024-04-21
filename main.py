import discord
from discord.ext import commands
from info import token
from discord.utils import get
import asyncio
from classes import HelperView, DocsView1
import random

random.seed(a=None, version=2)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
auth_channel1 = 1206656465616764998
guild_id = 1206656352857096312
news11_id = 1218168029288861757
news12_id = 1218168055386083369
news21_id = 1230165673926332477
news22_id = 1230165673985052733
role_name1g = "группа 1"
role_name2g = "группа 2"
role_name1y = "год 1"
role_name2y = "год 2"
bogdan_id = 416583789255327745


# не забыть заменить id на нужные!!!!!!!!!!!!!


@bot.command()
@commands.has_role("Admin")
async def split(ctx, *, mes):
    await ctx.message.delete()
    helpSplitTeams = mes.split(' ')

    finalTeams = []
    for i in range(len(helpSplitTeams) // 2):
        finalTeams.append([])
    for i in range(len(finalTeams)):
        for j in range(2):
            localHelpSplit = helpSplitTeams[random.randint(0, len(helpSplitTeams) - 1)]
            finalTeams[i].append(localHelpSplit)
            helpSplitTeams.remove(localHelpSplit)
    if len(helpSplitTeams) > 0:
        finalTeams[random.randint(0, len(finalTeams) - 1)].append(helpSplitTeams[0])

    await ctx.channel.send('Команды распределены:')
    for i in range(len(finalTeams)):
        localTeammates = f"{i + 1} - {' '.join(finalTeams[i])}"
        await ctx.channel.send(localTeammates)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="чем помочь ученикам Яндекс Лицея!"))


@bot.command()
async def question(ctx):
    user = ctx.message.author
    guild = ctx.guild
    member = user
    message_content = (f'Канал для вопроса учителю создан - тезисно напиши там свой вопрос. Чтобы удалить канал: '
                       f'```>delete_channel```')
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'Вопрос от {member}', overwrites=overwrites)
    global bogdan_id
    bogdan = user = await bot.fetch_user(bogdan_id)
    await channel.send(f"{user} хочет задать вопрос! {bogdan.mention}")
    await ctx.message.delete()


@bot.event
async def on_member_join(member):
    role = member.guild.get_role(role_id=1208730162414485555)
    await member.add_roles(role)


@bot.command()
@commands.has_role("new")
async def make_channel(ctx, name_msg1, name_msg2, name_msg3):
    user = ctx.author
    guild = ctx.guild
    member = user
    message_content = (f'Канал для аунтификации пользователя - "{member}" успешно создан! Выберите ваш ГОД и ГРУППУ '
                       f'обучния в соответсвующем канале.')
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'auth for {member}', overwrites=overwrites)
    await ctx.message.delete()

    name_msg = f"{name_msg1} {name_msg2} {name_msg3} под ником [ {member} ]"

    message1 = await channel.send('Выберите группу и год:\n1. Группа 1\n2. Группа 2')

    await message1.add_reaction('1️⃣')
    await message1.add_reaction('2️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        role1 = discord.utils.get(ctx.guild.roles, name='группа 1')
        role_str = "1 группу и"
    elif reaction.emoji == '2️⃣':
        role1 = discord.utils.get(ctx.guild.roles, name='группа 2')
        role_str = "2 группа и"
    else:
        await message1.delete()
        await channel.send('Ошибка... Вы что-то не так выбрали..')
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
        role_str = role_str + " 1ый год обучения"
    elif reaction.emoji == '2️⃣':
        role = discord.utils.get(ctx.guild.roles, name='год 2')
        role_str = role_str + " 2ой год обучения"
    else:
        await message.delete()
        await channel.send('Ошибка... Вы что-то не так выбрали.')
        return

    await message.delete()
    await channel.send('Выбор учтен.')

    global auth_channel1

    guild = bot.get_guild(guild_id)
    auth_channel = guild.get_channel(auth_channel1)

    check_mesaage = await auth_channel.send(f'Подтвердите действия {name_msg} - Он выбрал {role_str}')
    await check_mesaage.add_reaction('✅')
    await check_mesaage.add_reaction('❌')

    async def check(reaction, user):
        global bogdan_id
        logUser = user = await bot.fetch_user(bogdan_id)
        return user == logUser and str(reaction.emoji) in ['✅', '❌']

    try:
        reaction, _ = await bot.wait_for('reaction_add', timeout=None, check=check)
        if str(reaction.emoji) == '✅':
            await auth_channel.send("ОДОБРЕНО!")

            await user.send("ВАША ЗАЯВКА ОДОБРЕНА")

            await ctx.author.add_roles(role)
            await ctx.author.add_roles(role1)
            new_role = discord.utils.get(ctx.guild.roles, id=1208730162414485555, name="new")
            await ctx.author.remove_roles(new_role)
            await channel.send('Выбор подтвержден.')
            await channel.delete()
        elif str(reaction.emoji) == '❌':
            await auth_channel.send("НЕОДОБРЕНО!")

            await user.send("ВАША ЗАЯВКА НЕ ОДОБРЕНА")

            await channel.send('Выбор не поддтвержден')
            await channel.delete()
    except asyncio.TimeoutError:
        await ctx.send("You did not react in time. Eror 88002253535")


@bot.command()
@commands.has_role("Admin")
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
    message_content = (f'Руководство по использованию этого бота.\nВот все доступные команды:\n>question - создать '
                       f'канал для вопроса учителю.\n>docs - команда по выдачи документаций и полезных материалов для '
                       f'учеников!\n>admin_helper - для команд админа\nВыберите что бы Вы хотели бы узнать:')
    await user.send(message_content, view=HelperView())


@bot.command()
@commands.has_role("Admin")
async def admin_helper(ctx):
    await ctx.message.delete()
    user = ctx.message.author
    message_content = (">news - для создания новости\n>delete_channel - удалить канал\n>split ...(ученики через "
                       "пробел) - распределение по командам")
    await user.send(message_content)


@bot.command()
@commands.has_role("Admin")
async def news(ctx):
    guild = ctx.guild
    channel = ctx.channel
    await ctx.message.delete()

    message1 = await channel.send(
        'Выберите группу, которой написать объявление:\n1️⃣ - 1 группа 1 год\n2️⃣ - 2 группа 1 год\n3️⃣ - 1 группа 2 '
        'год\n4️⃣ - 2 группа 2 год\n0️⃣ - ВСЕМ')

    await message1.add_reaction('1️⃣')
    await message1.add_reaction('2️⃣')
    await message1.add_reaction('3️⃣')
    await message1.add_reaction('4️⃣')
    await message1.add_reaction('0️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '0️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        team11 = True
    elif reaction.emoji == '2️⃣':
        team12 = True
    elif reaction.emoji == '3️⃣':
        team21 = True
    elif reaction.emoji == '4️⃣':
        team22 = True
    elif reaction.emoji == '0️⃣':
        team11 = True
        team12 = True
        team21 = True
        team22 = True
    else:
        await message1.delete()
        await channel.send('Ошибка... Вы что-то не так выбрали.')
        return

    await message1.delete()
    await channel.send('Напишите объявление для этой группы:')
    announcement = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

    global role_name1g
    global role_name1y
    global role_name2g
    global role_name2y

    role_1g = discord.utils.get(ctx.guild.roles, name=role_name1g)
    role_2g = discord.utils.get(ctx.guild.roles, name=role_name2g)
    role_1y = discord.utils.get(ctx.guild.roles, name=role_name1y)
    role_2y = discord.utils.get(ctx.guild.roles, name=role_name2y)

    if team11:
        global news11_id
        news_channel = guild.get_channel(news11_id)
        await news_channel.send(f"{role_1g.mention}{role_1y.mention}\n" + announcement.content)
        await ctx.send("Объявление успешно переслано. 1 год 1 группа")

    if team12:
        global news12_id
        news_channel = guild.get_channel(news12_id)
        await news_channel.send(f"{role_2g.mention}{role_1y.mention}\n" + announcement.content)
        await ctx.send("Объявление успешно переслано. 1 год 2 группа")

    if team21:
        global news21_id
        news_channel = guild.get_channel(news21_id)
        await news_channel.send(f"{role_1g.mention}{role_2y.mention}\n" + announcement.content)
        await ctx.send("Объявление успешно переслано. 2 год 1 группа")

    if team22:
        global news22_id
        news_channel = guild.get_channel(news22_id)
        await news_channel.send(f"{role_2g.mention}{role_2y.mention}\n" + announcement.content)
        await ctx.send("Объявление успешно переслано. 2  год 2 группа")


@bot.command()
async def docs(ctx):
    user = ctx.message.author
    message_content = f'Вспомогательня информация по всей программе за 2 года обучения. Выберите свой год обучения!'
    await user.send(message_content, view=DocsView1())
    message = ctx.message
    await message.delete()


bot.run(token)
