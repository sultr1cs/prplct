import requests
import random
from io import BytesIO
from telegram import ChatAction, ParseMode
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater,ConversationHandler
import time
from colorama import init, Fore, Style

init()

welcome_green = f"{Fore.GREEN}Developed by{Style.RESET_ALL}"
welcome_purple = f"{Fore.MAGENTA}PurpleCat{Style.RESET_ALL}"

welcome_message = (''' 
  █░░░█ █▀▀ ▄▀▄ ▀█▀ █░░ █▀▀ █▀▀▄ 
  █░█░█ █▀▀ █▀█ ░█░ █▀▄ █▀▀ █▐█▀ 
  ░▀░▀░ ▀▀▀ ▀░▀ ░▀░ ▀░▀ ▀▀▀ ▀░▀▀

            █▀▄ ▄▀▄ ▀█▀ 
            █▀█ █░█ ░█░ 
            ▀▀░ ░▀░ ░▀░             ''')

print(welcome_message + '\n')
print(welcome_green)
print(welcome_purple)

def start(update, context):
    emoji = '☁️'
    start_text = ('''<pre>
  █░░░█ █▀▀ ▄▀▄ ▀█▀ █░░ █▀▀ █▀▀▄ 
  █░█░█ █▀▀ █▀█ ░█░ █▀▄ █▀▀ █▐█▀ 
  ░▀░▀░ ▀▀▀ ▀░▀ ░▀░ ▀░▀ ▀▀▀ ▀░▀▀

⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢰⡆⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣀⡤⡥⡄⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠤⠤⢰⡇⠀ ⠀⡶⠋⠉⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠳⢄⡼⠇⠀⠀⠀⠀⠉⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⣒⠒⠒⠒⠒⢒⡒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⣠⠄⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            █▀▄ ▄▀▄ ▀█▀ 
            █▀█ █░█ ░█░ 
            ▀▀░ ░▀░ ░▀░             </pre>
            я допоможу вам дізнатись 
             погоду у вашому місті.
            приємного користування❣️''')
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_text, parse_mode=ParseMode.HTML)
    time.sleep(3)
    context.bot.send_message(chat_id=update.effective_chat.id, text=emoji)
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Для того щоб дізнатись поточну погоду у вашому місті натисніть /w
    \nЯкщо ж ви хочете подивитись прогноз на декілька днів то нажміть /pw
    \nІнші команди - /help''')

def ask_city_w(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введіть назву міста: \n❌для скасування нажміть /cancel")
        return "GET_CITY_W"

def ask_city_pw(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введіть назву міста: \n❌для скасування нажміть /cancel")
    return "GET_CITY_PW"

def pw_handler(update, context):
    city = update.message.text

    sticker = 'CAACAgIAAxkBAAEJDCVkaWi4FgYIyf82_jHUrCYe3HMegQACgQEAAiteUwteCmw-bAABeLQvBA'
    sticker1 = 'CAACAgIAAxkBAAEJC61kaSmjhU8CKHuUj-5E7_TbeJiTSwACRQADWbv8JfvUpDThE_jrLwQ'
    random_sticker = random.choice([sticker, sticker1])

    sticker2 = 'CAACAgIAAxkBAAEJDC9kaWyUYy4iXrgm_lDKELBtRGbNRQACQgADWbv8Jd7Bb6A7P1vRLwQ'
    sticker3 = 'CAACAgIAAxkBAAEJDDFkaWytjYlEikF_Y72CyEVAYmvh_AAC9wAD9wLID9CX3j-K0TwOLwQ'
    sticker4 = 'CAACAgIAAxkBAAEJDDNkaWzeAeiv8KY-RzrNPZjhAwjBGQACpwADFkJrCtlzNEqUNHMpLwQ'
    random_sticker1 = random.choice([sticker2, sticker3, sticker4])

    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=random_sticker)
    context.bot.send_message(chat_id=update.effective_chat.id, text="💻пишу прогноз погоди...")

    time.sleep(2)

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_PHOTO)

    response = requests.get(f"https://wttr.in/{city}.png")
    photo = BytesIO(response.content)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=random_sticker1)

    return ConversationHandler.END

def w_handler(update, context):
    city = update.message.text

    sticker1 = 'CAACAgIAAxkBAAEJDC9kaWyUYy4iXrgm_lDKELBtRGbNRQACQgADWbv8Jd7Bb6A7P1vRLwQ'
    sticker2 = 'CAACAgIAAxkBAAEJDDFkaWytjYlEikF_Y72CyEVAYmvh_AAC9wAD9wLID9CX3j-K0TwOLwQ'
    sticker3 = 'CAACAgIAAxkBAAEJDDNkaWzeAeiv8KY-RzrNPZjhAwjBGQACpwADFkJrCtlzNEqUNHMpLwQ'
    random_sticker = random.choice([sticker1, sticker2, sticker3])

    stick1 = 'CAACAgIAAxkBAAEJCqRkaNNjesy3nKXFxLrlyHB8eK7R-AACBQEAAvcCyA_R5XS3RiWkoS8E'
    stick2 = 'CAACAgIAAxkBAAEJCrRkaNe5p-rDNbnZRJqzfzJXhL2BtwACjwADFkJrCr24snHVnwbiLwQ'
    stick3 = 'CAACAgIAAxkBAAEJC61kaSmjhU8CKHuUj-5E7_TbeJiTSwACRQADWbv8JfvUpDThE_jrLwQ'
    random_stick = random.choice([stick1, stick2, stick3])

    emoji1 = '🏙️Дізнаюсь поточну погоду...'
    emoji2 = '🌇Дізнаюсь поточну погоду...'
    random_emoji = random.choice([emoji1, emoji2])

    context.bot.send_message(chat_id=update.effective_chat.id, text=random_emoji)
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=random_stick)

    time.sleep(2)

    response = requests.get(f"https://wttr.in/{city}?0?q?T&lang=uk")
    formatted_text = f"<pre>. . . . . . . . . . . . . . . .\n{response.text}\n. . . . . . . . . . . . . . . .</pre>"
    context.bot.send_message(chat_id=update.effective_chat.id, text=formatted_text, parse_mode=ParseMode.HTML)
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=random_sticker)

    return ConversationHandler.END

def cancel(update, context):
    sticker = 'CAACAgIAAxkBAAEJDCdkaWsTod-MC3wHMQjvbEMLmLZr_gACxAADMNSdEcjFvLwK6xVKLwQ'
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введення скасовано.")
    context.bot.send_message(chat_id=update.effective_chat.id, sticker=sticker)
    return ConversationHandler.END

def handle_invalid_input(update, context):
    invalid_message = '''На жаль це не є командою, введіть команду /pw, щоб отримати прогноз погоди.
    \nТакож ви можете дізнатися поточну погоду у вашому місті написавши /w'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=invalid_message)

def random_fact(update, context):
    fact = 'У місцевості Калама, що в пустелі Атакама в Чилі, ніколи не йде дощ.'

    fact1 = 'Вологе повітря утримує тепло краще, ніж сухе. Тому ночі в пустелі дуже холодні, а у вологих тропіках fact = спекотні.'

    fact2 = 'У 1816 році на північному сході Сполучених Штатів морози і сніги спостерігалися протягом усіх 12 місяців. Подібні метеоумови переважали також у Франції, Італії та Іспанії. У США і Європі назвали 1816 рік “роком без літа”.'

    fact3 = 'Вдень хмари знаходяться вище, ніж вночі.'

    fact4 = 'У будь-який час в земній атмосфері відбувається близько 1800 гроз. Кожну секунду в землю вдаряє 100 блискавок.'

    fact5 = 'Веселку можна побачити вранці або ближче до вечора. Цей феномен спостерігається, коли сонце знаходиться на висоті 40 градусів над горизонтом або нижче.'

    fact6 = 'У Солт Лейк Сіті, штат Юта, в середньому щорічно випадає на 43 см снігу більше, ніж у Фербенксі, штат Аляска.'

    fact7 = 'У Санта-Фе, штат Нью-Мексико, щороку випадає на 23 см снігу більше, ніж в Нью-Хевен, штат Коннектикут.'

    fact8 = 'Професор Мічиганського університету Уолтер Коннор підрахував, що чоловіки в шість разів частіше уражаються блискавками, ніж жінки.'

    fact9 = 'У природі не існує двох сніжинок з абсолютно однаковою кристалічною структурою.'

    fact10 = 'Тисяча тонн космічного пилу щодня падає на землю.'

    fact11 = 'Взимку, коли будинок доводиться обігрівати, відносна вологість в середньостатистичному американському будинку становить 13%, що в два рази сушіше, ніж у пустелі Сахара.'

    fact12 = 'Дослідження в сучасному Китаї показали, що можна передбачати погоду з точністю до 80%, грунтуючись на квакання жаб. Селянин на ім’я Чанг Чи-цай розробив формулу, яку прийняли мільйони китайських фермерів і селян: Якщо в гарну погоду кумкає жаба, то через два дня буде дощ. Якщо жаба кумкає після дощу, погода покращиться. Дощ не вщухне, якщо вона не кумкає після кількох похмурих днів.'

    fact13 = 'Одного разу місто Тідікелт в пустелі Сахара не бачило дощу десять років.'

    fact14 = 'При ударі блискавки різниця потенціалів може досягати 100 мільйонів вольт.'

    fact15 = 'Під час великих бурь будівля Емпайр Стейт Білдінг може розгойдуватися на кілька футів в сторону.'

    fact16 = 'Щороку блискавки поставляють в землю 10 мільйонів тонн азоту.'

    random_fact = random.choice([fact, fact1, fact2, fact3, fact4, fact5, fact6, fact7, fact8, fact9, fact10, fact11, fact12, fact13, fact14, fact15, fact16 ])

    context.bot.send_message(chat_id=update.effective_chat.id, text=random_fact)

def help_handle(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='''💙Основні команди
    \n 🌈 /w - дізнатись поточну погоду у місті \n👀 /pw - дізнатись прогноз погоди по місту
    \n💛Додаткові команди
    \n 📚 /fact -  просто цікаві факти про погоду
    ''')

def main():
    updater = Updater("5990814038:AAFMPApcMzji-rSiL2Lrk6P2RHginEf7Mu8", use_context=True)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)

    random_fact_handler = CommandHandler('fact', random_fact)
    
    help_handler = CommandHandler('help', help_handle)

    invalid_input_handler = MessageHandler(Filters.text & ~Filters.command, handle_invalid_input)

    handler_w = ConversationHandler(
        entry_points=[CommandHandler('w', ask_city_w)],
        states={ "GET_CITY_W": [MessageHandler(Filters.text & ~Filters.command, w_handler)]},
        fallbacks=[CommandHandler('cancel', cancel)])

    handler_pw = ConversationHandler(
            entry_points=[CommandHandler('pw', ask_city_pw)],
            states={"GET_CITY_PW": [MessageHandler(Filters.text & ~Filters.command, pw_handler)]},
            fallbacks=[CommandHandler('cancel', cancel)])
     
    dp.add_handler(start_handler)
    dp.add_handler(handler_pw)
    dp.add_handler(handler_w)
    dp.add_handler(invalid_input_handler)
    dp.add_handler(random_fact_handler)
    dp.add_handler(help_handler)

    updater.start_polling()
    updater.idle()


main()
