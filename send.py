import telebot
import timeщ
bot = telebot.TeleBot('TOKEN')
# Чтение содержимого текстового файла
with open('/opt/pars/feed.txt', 'r') as file:
    file_content = file.read()
news=file_content.split("\n\n")
#print(news)
for element in news:
      if element:
           bot.send_message(chat_id='CHAT_ID', text=element)
      time.sleep(3)
