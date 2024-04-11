import discord
from discord.ext import commands
from info import token
from discord.utils import get
from discord import ui, app_commands
import datetime
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
auth_channel1 = 1206656465616764998
guild_id = 1206656352857096312
news1_id = 1218168029288861757
news2_id = 1218168055386083369
#не забыть заменить id на нужные!!!!!!!!!!!!!

class HelperView(discord.ui.View):
    @discord.ui.button(label="Как задать вопрос учителю?", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, interaction, button):
        await interaction.response.send_message("В специальном тексковом канале пишите команду - >question")

    @discord.ui.button(label="Все команды", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button):
        await interaction.response.send_message("Вот все доступные команды:\n>question - создать канал для вопроса учителю.\n>docs - команда по выдачи документаций и полезных материалов для учеников!")


class DocsView3(discord.ui.View):
    @discord.ui.button(label="PyQt5", row=0, style=discord.ButtonStyle.primary)
    async def firstProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://doc.qt.io/qtforpython-5/contents.html \nУдобное краткое руководство - https://translated.turbopages.org/proxy_u/en-ru.ru.2ace4ec1-660bcb43-5c3e9812-74722d776562/https/www.tutorialspoint.com/pyqt5/pyqt5_quick_guide.htm \nВидео про кнопки на англ. - https://www.youtube.com/watch?time_continue=423&v=-2uyzAqefyE&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \nВидео про простейший калькултор на PyQt5 - https://www.youtube.com/watch?time_continue=292&v=7aAF0s7-5io&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \n Туториал по работе с PyQt5 и QtDesigner (Создание гениратора паролей) -  https://www.youtube.com/watch?time_continue=454&v=pMNrxE1xAfw&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \nКоманды для import библеотек: \n```pip install PyQt5Designer```\n```pip install PyQt5```", view=DocsView3())

    @discord.ui.button(label="SQL Базы данных", row=1, style=discord.ButtonStyle.primary)
    async def secondProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Скачать SQLiteStudio - https://sqlitestudio.pl/ \nSQLiteStudio как пользоваться - https://www.youtube.com/watch?v=QH_wPA0ojRc \nБольшая практическая шпаргалка SQL (SQLite) с готовыми запросами - https://habr.com/ru/articles/792630/ \nКомнада для добавления бибилеотки: ```pip install pymysql```", view=DocsView3())

    @discord.ui.button(label="PyGame", row=0, style=discord.ButtonStyle.primary)
    async def thirdProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://pygame-docs.website.yandexcloud.net/ref/pygame.html \nВидео как сделать игру на весь экран - https://www.youtube.com/watch?v=wP7PJohQOMc \nВидео как сделать меню - https://www.youtube.com/watch?v=kqrlD8X8pdw \nШпаргалка - https://waksoft.susu.ru/2019/04/24/pygame-shpargalka-dlja-ispolzovanija/ \nКоманда для import - ```pip install pygame```", view=DocsView3())

    @discord.ui.button(label="Flusk", row=1, style=discord.ButtonStyle.primary)
    async def fourthProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://flask.palletsprojects.com/en/3.0.x/ \nFlusk шпаргалка(англ) - https://codeinsightacademy.com/blog/python/flask-cheat-sheet/ \nFlask работа с базой данных - https://www.youtube.com/watch?v=_CwCk5g8YJg&t=2s \nКоманда для import -```pip install Flask```", view=DocsView3())

    @discord.ui.button(label="Остальные", row=1, style=discord.ButtonStyle.primary)
    async def fiveProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация по телеграм боту - https://docs.python-telegram-bot.org/en/stable/index.html \nОфициальная документация по дискорд боту - https://discordpy.readthedocs.io/en/stable/index.html \nКомнады для import:\n```pip install discord.py```\n```pip install pyTelegramBotAPI```", view=DocsView3())


class DocsView2(discord.ui.View):
    @discord.ui.button(label="Скачивание IDE и настройка", row=0, style=discord.ButtonStyle.primary)
    async def firstModule_button_callback(self, interaction, button):
        await interaction.response.send_message("Видео итструкция (не официальная) - https://yandex.ru/video/preview/12460819480399738578 \nСсылка на скачивание с сайта разработчиков - https://www.jetbrains.com/pycharm-edu/ \n", view=DocsView2())

    @discord.ui.button(label="Вспомогательная информация при ихучении Python", row=1, style=discord.ButtonStyle.primary)
    async def secondModule_button_callback(self, interaction, button):
        await interaction.response.send_message("Вспомогательный курс по Python - https://itproger.com/course/python \n Удобная документация - https://www.python.org/doc/ \n Комнадна для обновления pip - ``` python -m pip install --upgrade pip```", view=DocsView2())

class DocsView1(discord.ui.View):
    @discord.ui.button(label="1 ГОД обучения", row=0, style=discord.ButtonStyle.primary, emoji="🤓")
    async def firstYear_button_callback(self, interaction, button):
        await interaction.response.send_message("Какой модуль в 1ом году вас интересует?", view=DocsView2())

    @discord.ui.button(label="2 ГОД обучения", row=1, style=discord.ButtonStyle.primary, emoji="😎")
    async def secondYear_button_callback(self, interaction, button):
        await interaction.response.send_message("Какая тема вас инетерисует в 2ом году?", view=DocsView3())


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="чем помочь ученикам Яндекс Лицея!"))

@bot.command()
async def question(ctx):
    user = ctx.message.author
    guild = ctx.guild
    member = user
    message_content = f'Канал для вопроса учителю создан - тезисно напиши там свой вопрос. Чтобы удалить канал: ```>delete_channel```'
    await user.send(message_content)
    admin_role = get(guild.roles, name="Admin")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True),
        admin_role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await guild.create_text_channel(f'Вопрос от {member}', overwrites=overwrites)
    await channel.send(f"@{user} хочет задать вопрос! @wander1ust_")
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
        await ctx.send("You did not react in time. Eror 88002253535")


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
    message_content = f'Руководство по использованию этого бота.\nВот все доступные команды:\n>question - создать канал для вопроса учителю.\n>docs - команда по выдачи документаций и полезных материалов для учеников!\nВыберите что бы Вы хотели бы узнать:'
    await user.send(message_content, view=HelperView())


@bot.command()
@commands.has_role("Admin")
async def news(ctx):
    user = ctx.author
    guild = ctx.guild
    member = user
    channel = ctx.channel
    await ctx.message.delete()

    name_msg = member

    message1 = await channel.send('Выберите группу, которой написать объявление:\n1. Группа 1\n2. Группа 2')

    await message1.add_reaction('1️⃣')
    await message1.add_reaction('2️⃣')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['1️⃣', '2️⃣']

    reaction, _ = await bot.wait_for('reaction_add', timeout=60.0, check=check)

    if reaction.emoji == '1️⃣':
        team1 = True
    elif reaction.emoji == '2️⃣':
        team1 = False
    else:
        await message1.delete()
        await channel.send('Ошибка... Вы что-то не так выбрали.')
        return

    await message1.delete()
    await channel.send('Напишите объявление для этой группы:')
    announcement = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

    if team1:
        global news1_id
        news_channel = guild.get_channel(news1_id)
        await news_channel.send(announcement.content)
        await ctx.send("Объявление успешно переслано.")

    else:
        global news2_id
        news_channel = guild.get_channel(news2_id)
        await news_channel.send(announcement.content)
        await ctx.send("Объявление успешно переслано.")


@bot.command()
async def docs(ctx):
    user = ctx.message.author
    message_content = f'Вспомогательня информация по всей программе за 2 года обучения. Выберите свой год обучения!'
    await user.send(message_content, view=DocsView1())
    message = ctx.message
    await message.delete()


#bot.run(token, bot=True)
bot.run("MTIwNjY1NzE4MjEzNzg1MTk5NA.G-QwzL.fYiWP2cgJsOdM-_jE1_4DYLGt468YQdrRc4urY")
