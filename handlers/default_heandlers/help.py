from loader import bot


@bot.message_handler(commands=['help', 'reset'])
def help(message):
    bot.send_message(chat_id=message.chat.id, text='/lowprice - cheap hotels\n'
                                      '/highprice - expensive hotels\n'
                                      '/bestdeal - custom hotel searching\n'
                                      '/history - show history\n'
                                      '/reset - get back to menu')


@bot.callback_query_handler(func= lambda call: call.data == 'restart')
def help(call):
    bot.send_message(chat_id=call.message.chat.id, text='/lowprice - cheap hotels\n'
                                      '/highprice - expensive hotels\n'
                                      '/bestdeal - custom hotel searching\n'
                                      '/history - show history\n'
                                      '/reset - get back to menu')
