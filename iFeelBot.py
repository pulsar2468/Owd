import sqlite3
import telepot
import re
import datetime
import requests

def Julia_handle(message):
        id_sender, msg, chat_id = message['from']['id'],message['text'],message['chat']['id']
        if len(msg.split()) < 2: return
        what, name=msg.split(' ',1)

        if (what == "weather" and name== "list"):
            url = 'http://192.168.1.111:8001/list_files'
            r = requests.get(url)
            bot.sendMessage(chat_id, r.text)
            return

        if (what == "weather"):
            url = 'http://192.168.1.111:8001/%s' % name
            r = requests.get(url)
            if (r.status_code == 404):
                bot.sendSticker(chat_id,stickers[0])
                bot.sendMessage(chat_id, "At this time, the file not exists!")
            else:
                bot.sendMessage(chat_id, r.text)
            return

        city_list = []
        sql2 = 'SELECT City.name FROM City'
        conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
        c = conn.cursor()

        for row in c.execute(sql2):
            city_list.append(row[0])

        if name in city_list:
            latest_list = []

            #####To get last data######
            if re.search('[Tt]emperature|[Tt]emp', what):

                sql1 = 'SELECT "%s".temp ' \
                          'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                          name, name, name, name, name)



                for row in c.execute(sql1):
                    latest_list.append(row[0])

                bot.sendMessage(chat_id,'Last Temp: '+str(latest_list))
                conn.close()
                return

            if re.search('[Hh]umidity|[Hh]um', what):

                    sql1 = 'SELECT "%s".humidity ' \
                          'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                          name, name, name, name, name)

                    for row in c.execute(sql1):
                        latest_list.append(row[0])

                    bot.sendMessage(chat_id,'Last humidity: '+str(latest_list))
                    conn.close()
                    return

            if re.search('[Ww]ind', what):

                    latest_list = []
                    sql1 = 'SELECT "%s".wind_speed ' \
                          'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                          name, name, name, name, name)



                    for row in c.execute(sql1):
                            latest_list.append(row[0])

                    bot.sendMessage(chat_id,'Last Wind Speed: '+str(latest_list))
                    conn.close()
                    return

            if re.search('[Aa]ll', what):
                    sql1 = 'SELECT City.id,"%s".name,"%s".detection_time,' \
                          'City.lat,City.lon,"%s".temp,"%s".humidity,"%s".wind_speed ' \
                          'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")' % (
                           name, name, name, name, name, name, name, name,name)


                    for row in c.execute(sql1):
                            latest_list.append(row)

                    bot.sendMessage(chat_id,'Temperature: '+str(latest_list[0][5])+'\n'+'Humidity: '+str(latest_list[0][6])+'\n'+'Wind Speed: '+str(latest_list[0][7]*3.6)+' km/h')
                    conn.close()
                    return



                ####History####

            if re.search('[Hh]istory', what):

                        sql1 = 'SELECT "%s".detection_time,"%s".temp,"%s".humidity,"%s".wind_speed FROM "%s" ORDER BY "%s".rowid DESC '\
                               'LIMIT 10' % (name,name,name,name,name,name)

                        dT=[]
                        temp=[]
                        hum=[]
                        wind=[]
                        result=''

                        for row in c.execute(sql1):
                            latest_list.append(row)

                        for i in range(0, len(latest_list)):
                            dT.append(datetime.datetime.strptime(latest_list[i][0], "%Y-%m-%d %H:%M:%S"))
                            temp.append(latest_list[i][1])
                            hum.append(latest_list[i][2])
                            wind.append(latest_list[i][3])

                        for x,y,w,z in zip(dT,temp,hum,wind):
                            result=result +'Date Detection: %s\nTemperature: %s\nHumidity: %s\nWind Speed: %s\n\n' %(x,y,w,z)

                        bot.sendMessage(chat_id,result)
                        conn.close()
                        return
                        ###########################


        else:
            bot.sendSticker(chat_id,stickers[1])
            bot.sendMessage(chat_id, 'You don\'t want to see him angry.\n\nCity not found! Please  choose between these..\n' + str(city_list))


stickers = ['CAADBAADFwUAAv-4-AVj7lOYcpBoKAI','CAADBAADJQUAAv-4-AXgwpxLWFOwJwI']
bot = telepot.Bot('')
bot.message_loop(Julia_handle,run_forever=True)
#stickers[0] Not exists,
#stickers[1] Angry Chuck

#while 1: it's equivalent to run_forever=True
    #time.sleep(10)
