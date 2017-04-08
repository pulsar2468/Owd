import sqlite3


def history_table(name, lon, lat, pressure, temp, humidity, wind_speed, t, id):
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql=""

    for i in name:
        sql = sql +  'CREATE TABLE IF NOT EXISTS "%s" ("id" VARCHAR PRIMARY KEY, ' \
          '"temp" FLOAT, "humidity" FLOAT, "wind_speed" FLOAT, ' \
          '"detection_time" DATETIME);' %i

    sql=sql+'CREATE TABLE IF NOT EXISTS City ("id" VARCHAR PRIMARY KEY, "name" FLOAT, "lat" FLOAT, "lon" FLOAT);'
    c.executescript(sql)
    conn.commit()
    conn.close()


def drop_table(name):
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql=""

    for i in name:
        sql = sql +  'DROP TABLE IF EXISTS "%s";' %i

    sql=sql+ 'DROP TABLE IF EXISTS City;'
    conn.executescript(sql)
    conn.close()


def insert_city(name, lon, lat, id):
   conn= sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
   c = conn.cursor()
   sql = ""

   for i,n,l,ln in zip(id,name,lat,lon):
       sql = sql + 'INSERT or IGNORE INTO City  VALUES ("%s","%s",%f,%f);' %(i,n,l,ln)

   c.executescript(sql)
   conn.commit()
   conn.close()


def insert_history_city(name,temp, humidity, wind_speed, t, id):
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = ""

    for a1,b1,c1,d1,e1,f1 in zip(id,temp, humidity, wind_speed, t,name):
        sql = sql + 'INSERT or IGNORE INTO "%s" VALUES ("%s",%f,%f,%f,"%s");' % (f1,a1,b1,c1,d1,e1)

    sql = sql + 'CREATE TABLE IF NOT EXISTS City ("id" VARCHAR PRIMARY KEY, "name" FLOAT, "lat" FLOAT, "lon" FLOAT);'
    c.executescript(sql)
    conn.commit()
    conn.close()


