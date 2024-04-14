import discord
from discord.ext import commands
from info import token
from discord.utils import get
from discord import ui, app_commands
import datetime
import asyncio
import os
class HelperView(discord.ui.View):
    @discord.ui.button(label="Как задать вопрос учителю?", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, interaction, button):
        await interaction.response.send_message("В специальном тексковом канале пишите команду - >question", view=HelperView())

    @discord.ui.button(label="Все команды", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button):
        await interaction.response.send_message("Вот все доступные команды:\n>question - создать канал для вопроса учителю.\n>docs - команда по выдачи документаций и полезных материалов для учеников!", view=HelperView())


class DocsView3(discord.ui.View):
    @discord.ui.button(label="PyQt5", row=0, style=discord.ButtonStyle.primary)
    async def firstProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://doc.qt.io/qtforpython-5/contents.html \nУдобное краткое руководство - https://translated.turbopages.org/proxy_u/en-ru.ru.2ace4ec1-660bcb43-5c3e9812-74722d776562/https/www.tutorialspoint.com/pyqt5/pyqt5_quick_guide.htm \nВидео про кнопки на англ. - https://www.youtube.com/watch?time_continue=423&v=-2uyzAqefyE&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \nВидео про простейший калькултор на PyQt5 - https://www.youtube.com/watch?time_continue=292&v=7aAF0s7-5io&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \n Туториал по работе с PyQt5 и QtDesigner (Создание гениратора паролей) -  https://www.youtube.com/watch?time_continue=454&v=pMNrxE1xAfw&embeds_referring_euri=https%3A%2F%2Fyastatic.net%2Fvideo-player%2F0xe7891f6f377%2Fpages-common%2Fyoutube%2Fyoutube.html&source_ve_path=Mjg2NjY&feature=emb_logo \nКоманды для import библеотек: \n```pip install PyQt5Designer```\n```pip install PyQt5```", view=DocsView3())

    @discord.ui.button(label="SQL Базы данных", row=1, style=discord.ButtonStyle.primary)
    async def secondProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Скачать SQLiteStudio - https://sqlitestudio.pl/ \nSQLiteStudio как пользоваться - https://www.youtube.com/watch?v=QH_wPA0ojRc \nБольшая практическая шпаргалка SQL (SQLite) с готовыми запросами - https://habr.com/ru/articles/792630/ \nКомнада для добавления иной удобной бибилеотки: ```pip install pymysql```", view=DocsView3())

    @discord.ui.button(label="PyGame", row=0, style=discord.ButtonStyle.primary)
    async def thirdProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://pygame-docs.website.yandexcloud.net/ref/pygame.html \nВидео как сделать игру на весь экран - https://www.youtube.com/watch?v=wP7PJohQOMc \nВидео как сделать меню - https://www.youtube.com/watch?v=kqrlD8X8pdw \nШпаргалка - https://waksoft.susu.ru/2019/04/24/pygame-shpargalka-dlja-ispolzovanija/ \nКоманда для import - ```pip install pygame```", view=DocsView3())

    @discord.ui.button(label="Flask", row=1, style=discord.ButtonStyle.primary)
    async def fourthProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация - https://flask.palletsprojects.com/en/3.0.x/ \nFlask шпаргалка(англ) - https://codeinsightacademy.com/blog/python/flask-cheat-sheet/ \nFlask работа с базой данных - https://www.youtube.com/watch?v=_CwCk5g8YJg&t=2s \nКоманда для import -```pip install Flask```", view=DocsView3())

    @discord.ui.button(label="Остальное", row=1, style=discord.ButtonStyle.primary)
    async def fiveProject_button_callback(self, interaction, button):
        await interaction.response.send_message("Официальная документация по телеграм боту - https://docs.python-telegram-bot.org/en/stable/index.html \nОфициальная документация по дискорд боту - https://discordpy.readthedocs.io/en/stable/index.html \nКомнады для import:\n```pip install discord.py```\n```pip install pyTelegramBotAPI```", view=DocsView3())

    @discord.ui.button(label="Назад", row=3, style=discord.ButtonStyle.gray)
    async def home_button(self, interaction, button):
        await interaction.response.send_message("Выберите год обучниея.", view=DocsView1())



class DocsView2(discord.ui.View):
    @discord.ui.button(label="Скачивание IDE и настройка", row=0, style=discord.ButtonStyle.primary)
    async def firstModule_button_callback(self, interaction, button):
        await interaction.response.send_message("Видео как скачать python - https://yandex.ru/video/preview/11147201474752498360 \nВидео итструкция (не официальная) - https://yandex.ru/video/preview/12460819480399738578 \nСсылка на скачивание с сайта разработчиков - https://www.jetbrains.com/pycharm-edu/ \n", view=DocsView2())

    @discord.ui.button(label="Вспомогательная информация при изучении Python", row=1, style=discord.ButtonStyle.primary)
    async def secondModule_button_callback(self, interaction, button):
        await interaction.response.send_message("Вспомогательный курс по Python - https://itproger.com/course/python \n Удобная документация - https://www.python.org/doc/ \n Комнадна для обновления pip - ``` python -m pip install --upgrade pip```", view=DocsView2())

    @discord.ui.button(label="Назад", row=3, style=discord.ButtonStyle.gray)
    async def home_button(self, interaction, button):
        await interaction.response.send_message("Выберите год обучниея.", view=DocsView1())

class DocsView1(discord.ui.View):
    @discord.ui.button(label="1 ГОД обучения", row=0, style=discord.ButtonStyle.primary, emoji="🤓")
    async def firstYear_button_callback(self, interaction, button):
        await interaction.response.send_message("Какой модуль в 1ом году вас интересует?", view=DocsView2())

    @discord.ui.button(label="2 ГОД обучения", row=1, style=discord.ButtonStyle.primary, emoji="😎")
    async def secondYear_button_callback(self, interaction, button):
        await interaction.response.send_message("Какая тема вас инетерисует в 2ом году?", view=DocsView3())