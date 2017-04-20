import sqlite3
import telepot
import re


# funzione che viene eseguita ad ogni messaggio ricevuto

def Julia_handle(message):
        id_sender, msg, chat_id = message['from']['id'],message['text'],message['chat']['id']
        if len(msg.split()) < 2: return
        what, name=msg.split(' ',1)

        if re.search('[Tt]emperature|[Tt]emp', what):
            latest_list = []

            conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
            c = conn.cursor()
            sql = 'SELECT "%s".temp ' \
                  'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                  name, name, name, name, name)
            for row in c.execute(sql):
                latest_list.append(row)
            conn.close()
            bot.sendMessage(chat_id,str(latest_list[0]))



bot = telepot.Bot('345541407:AAHs9hnV1T7f3Nq1f4qVoK6IpwjkyxYG3GM')
bot.message_loop(Julia_handle,run_forever=True)
#while 1: it's equivalent to run_forever=True
    #time.sleep(10)