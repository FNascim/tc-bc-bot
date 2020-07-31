from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='1325068965:AAF5juNZggOljPkkxe3N4cdr2jwyfvsuDX4')  # Telegram API Token
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Para ir ao site digite /site\n'
                                                          'Para informações sobre o cartão digite /cartao\n'
                                                          'Para informações sobre seguros digite /seguros\n'
                                                          'Para parcelar fatura digite /parcelar\n'
                                                          'Para segunda via de boleto digite /boleto\n'
                                                          'Para saber nossos telefones de contato digite /telefones\n'
                                                          'Como posso te ajudar?')

def site(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='https://www.carrefoursolucoes.com.br')

def cartao(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='https://www.carrefoursolucoes.com.br/cartao/beneficios')

def seguros(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='https://www.carrefoursolucoes.com.br/seguros1')

def parcelar(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='https://www.carrefoursolucoes.com.br/servicos/parcele')

def telefones(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Atendimento Eletrônico\n'
                                                          'De segunda a sábado das 08h00 às 21h00\n'
                                                          'São Paulo e Regiões Metropolitanas\n'
                                                          '3004 2222\n'
                                                          'Demais Localidades\n'
                                                          '0800 718 2222')

def boleto(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='https://www.carrefoursolucoes.com.br/auto-atendimento')

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Desculpe, não entendi!")


start_command_handler = CommandHandler('start', startCommand)
site_handler = CommandHandler('site',site)
unknow_handler = MessageHandler(Filters.command, unknown)
cartao_handler = CommandHandler('cartao',cartao)
boleto_handler = CommandHandler('boleto',boleto)
telefones_handler = CommandHandler('telefones',telefones)
parcelar_handler = CommandHandler('parcelar',parcelar)
seguros_handler = CommandHandler('seguros',seguros)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(site_handler)
dispatcher.add_handler(cartao_handler)
dispatcher.add_handler(boleto_handler)
dispatcher.add_handler(telefones_handler)
dispatcher.add_handler(parcelar_handler)
dispatcher.add_handler(seguros_handler)
dispatcher.add_handler(unknow_handler)

updater.start_polling(clean=True)
#Ctrl + C parar o bot
updater.idle()
