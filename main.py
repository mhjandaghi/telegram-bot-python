import telebot

bot = telebot.TeleBot('7105336167:AAHzeeHC00K6QRSA_EefIRP9VGamQVrkvWw')
first_button = telebot.types.InlineKeyboardButton('ارتباط با سازنده', url= 'https://t.me/mhdi_jay') # دکمه شیشه ای
twice_button = telebot.types.InlineKeyboardButton('گروه مــــادو', url= 'https://madev.ir') 
third_button = telebot.types.InlineKeyboardButton("آیدی بدکست", callback_data='BedCast')
markup = telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button, twice_button, third_button) # اضافه کردن دکمه شیشه ای
# -----
key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) # دکمه کیبوردی
key_markup.add("ترجمه شماره", 'درباره ما', 'حمایت مالی', 'آشنایی با بِد گروپ', row_width=2) # اضافه کزدن دکمه کیبورذی
# ----- 
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    bot.answer_callback_query(call.id, "@Bed_Cast", show_alert=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'سلام به ربات کاربردی نامترانس خوش اومدی \n برای استفاده از قابلیت اصلی /translate رو وارد کن.', reply_markup=key_markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'این ربات توسط @mhdi_jay طراحی شده \n برای انتقادات و پیشنهادات خودتون پیام بدید.', reply_markup=markup)

@bot.message_handler()
def keyboard(message):
    if message.text == 'ترجمه شماره':
        bot.send_message(message.chat.id, " شماره مورد نظر خودت رو وارد کن")
    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, 'من مهدی ام و از طرف گروه مادو این ربات برات ساختم تا بتونی شماره های فارسی به سرعت انگلیسی کنی \nبرای ارتباط با ما '
                         'رو یکی از دکمه های بزنی', reply_markup=markup)
    elif message.text == 'حمایت مالی':
        bot.send_message(message.chat.id, 'بزودی بلادی خودم')
    elif message.text == 'آشنایی با بِد گروپ':
        bot.send_message(message.chat.id, 'اونم به موقعش معرفی میشه!')

@bot.message_handler(func= lambda m:True)
def number(message):
    if message.text == 'ترجمه شماره':
        num = bot.send_message(message.chat.id, 'نام خود را وارد کنید')
        bot.register_next_step_handler(num, answer)

def answer(message):
    global numeric
    numeric = message.text

bot.infinity_polling()

  