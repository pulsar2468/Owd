import sqlite3
import telepot
import re




def Julia_handle(message):
        id_sender, msg, chat_id = message['from']['id'],message['text'],message['chat']['id']
        if len(msg.split()) < 2: return
        what, name=msg.split(' ',1)

        if re.search('[Tt]emperature|[Tt]emp', what):

            latest_list = []
            city_list = []
            conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
            c = conn.cursor()
            sql1 = 'SELECT "%s".temp ' \
                  'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                  name, name, name, name, name)

            sql2='SELECT City.name FROM City'
            for row in c.execute(sql2):
                city_list.append(row[0])

            if name in city_list:

                for row in c.execute(sql1):
                    latest_list.append(row[0])

                bot.sendMessage(chat_id,'Last Temp: '+str(latest_list))
            else:
                bot.sendMessage(chat_id,'City not found! Please choose between these..\n'+str(city_list))

            conn.close()
        if re.search('[Hh]umidity|[Hh]um', what):

            latest_list = []
            city_list = []
            conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
            c = conn.cursor()
            sql1 = 'SELECT "%s".humidity ' \
                  'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                  name, name, name, name, name)

            sql2='SELECT City.name FROM City'
            for row in c.execute(sql2):
                city_list.append(row[0])

            if name in city_list:

                for row in c.execute(sql1):
                    latest_list.append(row[0])

                bot.sendMessage(chat_id,'Last humidity: '+str(latest_list))
            else:
                #bot.sendMessage(chat_id,'City not found! Please  choose between these..\n'+str(city_list))
                bot.sendSticker(chat_id)

            conn.close()



bot = telepot.Bot('345541407:AAHs9hnV1T7f3Nq1f4qVoK6IpwjkyxYG3GM')
bot.message_loop(Julia_handle,run_forever=True)
stickers = ['']
#while 1: it's equivalent to run_forever=True
    #time.sleep(10)