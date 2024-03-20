import telebot

token = "xxx"  #API

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
     welcome = (' Привет, я умный бот!\n\n '
                '/start - запустить бота! \n '
                '/class - показать список класса \n '
                '/help - рассказать, что я умею? (после запуска)')
     bot.send_message(message.from_user.id, welcome)


@bot.message_handler(commands=['help'])
def send_info(message):
     info = ('Я могу рассказать Вам об успеваемости Вашего ребенка. '
             'Просто введите фамилию и все данные тут же отправятся на Ваш телефончик)\n\n'
             '/class - показать список класса \n '
             '/help - рассказать, что я умею? (после запуска)')

     bot.send_message(message.from_user.id, info)


grade= {'иваненко':{ 'Английский язык': 5, 'Математика': 4,'Русский язык': 5,'Биология': 3,'География': 5,'История': 4},
        'лазаренко':{ 'Английский язык': 5, 'Математика': 5,'Русский язык': 5,'Биология': 5,'География': 5,'История': 5},
        'никитин':{ 'Английский язык': 4, 'Математика': 5,'Русский язык': 4,'Биология': 4,'География': 5,'История': 5},
        'орехов':{ 'Английский язык': 5, 'Математика': 5,'Русский язык': 4,'Биология': 4,'География': 5,'История': 4},
        'стиранивский':{ 'Английский язык': 3, 'Математика': 3,'Русский язык': 4,'Биология': 5,'География': 3,'История': 5},
        'суковина':{ 'Английский язык': 3, 'Математика': 5,'Русский язык': 4,'Биология': 5,'География': 3,'История': 5},
        }

objects = ['Английский язык', 'Математика','Русский язык','Биология','География','История']
spisok = ['иваненко', 'лазаренко', 'никитин', 'орехов', 'стиранивский', 'суковина']
spisok_for_user = ['Иваненко', 'Лазаренко', 'Никитин', 'Орехов', 'Стиранивский', 'Суковина']


@bot.message_handler(commands= ['class'])
def send_class_list(message):
    string = 'Список класса:\n\n'

    for i in range(0, len(spisok_for_user)):
        string += spisok_for_user[i] + '\n'

    bot.send_message(message.from_user.id, string)
    bot.send_message(message.from_user.id, 'Введите фамилию Вашего ребенка')


@bot.message_handler(content_types=['text'])
def get_lastname(message):
    grades = 'Успеваемость вашего ребенка (' + str(message.text).upper() + ') :\n\n'

    if (message.text.lower() in spisok) :

        j = 0

        for i in grade[message.text.lower()]:
            grades += str(objects[j]) + ' - ' + str(grade[message.text.lower()][i]) + '\n'
            j += 1
        bot.send_message(message.from_user.id, grades)
        bot.send_message(message.from_user.id,'/class - вот список класса\n'
                                              '/help - что я умею')

    else:
        bot.send_message(message.from_user.id, 'Такой фамилии нет в списке(\n'
                                               'Попробуйте еще раз\n\n '
                                               '/class - вот список класса')


bot.polling()