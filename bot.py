from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import planets


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info("бот запускается")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", check_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Добро пожаловать'
    logging.info(text)
    update.message.reply_text(text)



def talk_to_me(bot, update):
    user_text =  "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat_id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)
    if update.message.text == 'Mars':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.mars)))
    if update.message.text == 'Jupiter':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.jupiter)))
    if update.message.text == 'Mercury':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.mercury)))
    if update.message.text == 'Venus':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.venus)))
    if update.message.text == 'Saturn':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.saturn)))
    if update.message.text == 'Uranus':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.uranus)))
    if update.message.text == 'Neptune':
            update.message.reply_text\
                ('Планета сегодня в созвездии {}'.format
                 (ephem.constellation(planets.neptune)))


def check_planet(bot, update):
    user_planet = 'Введите название планеты латиницей'
    logging.info(user_planet)
    update.message.reply_text(user_planet)
    logging.info(update.message.text)


main()
greet_user()
talk_to_me()
check_planet()