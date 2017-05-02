import telegram

bot_token = '344532609:AAG8LgfCK9U0UpBTgczDeEU-zaW3P4vFHno'

bot = telegram.Bot(token=bot_token)
last_update_id = None
for update in bot.getUpdates():
    print(update.message)
    last_update_id = update['update_id']
    chat_id = update.message.chat.id
    user = update.message.from_user
    username = "{0} {1}".format(user.first_name, user.last_name)
    bot.sendMessage(chat_id, 'Привет, {0}'.format(username))

print(last_update_id)
