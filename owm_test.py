import datetime
import requests
import time

import owm_beta1


def post_value():
    url = 'http://api.openweathermap.org/data/3.0/measurements?appid=e229425a7ad4dc9b361f341f7ce03904'
    payload = [{
    "station_id": "58da60d7be85b200010eee82",
    "dt": int(time.time()),
    "temperature": 1.7,
    "wind_speed": 1.9,
    "wind_deg":28,
    "humidity": 80,
    }]


    # GET with params in URL
    r = requests.post(url, json=payload)
    print(r.status_code)
    print(r.text)


def get_value():
    url = 'http://api.openweathermap.org/data/3.0/measurements?appid=e229425a7ad4dc9b361f341f7ce03904'

    date_entry = input('Enter a date in YYYY-MM-DD-HH-MM format')
    year, month, day, hours, minutes = map(int, date_entry.split('-'))
    from_date0 = datetime.datetime(year, month, day, hours, minutes)

    #date_entry1 = input('Enter a date in YYYY-MM-DD-HH-MM format')
    #year1, month1, day1, hours1, minutes1 = map(int, date_entry1.split('-'))
    #to_date1 = datetime.datetime(year1, month1, day1, hours1, minutes1)

    payload = {
        "type": "m",
        "limit":100,
        "from": int(time.mktime(from_date0.timetuple())),
        "to": int(time.time()) ,
        "station_id": "58da60d7be85b200010eee82",
    }
    # GET with params in URL
    r = requests.get(url,params=payload)
    print(r.status_code, r.text)


def get_stations():
    url = 'http://api.openweathermap.org/data/3.0/stations?appid=e229425a7ad4dc9b361f341f7ce03904'
    # GET with params in URL
    r = requests.get(url)
    print(r.status_code, r.text)


def delete_stations():
    url = 'http://api.openweathermap.org/data/3.0/stations/##################?appid=e229425a7ad4dc9b361f341f7ce03904' #insert your idStation!
    # GET with params in URL
    r = requests.delete(url)
    print(r.status_code, r.text)


def create_station():
    url = 'http://api.openweathermap.org/data/3.0/stations?appid=e229425a7ad4dc9b361f341f7ce03904'

    payload = {
        "external_id": "P_test0",
        "name": "PalermoTestStation",
        "latitude": 38.1156879,
        "longitude": 13.3612,
        "altitude": 20
    }

    #headers = {'Content-Type': 'application/json'}

    # GET with params in URL
    r = requests.post(url, json=payload)
    print(r.status_code,r.text)


def get_value_from_rectangle():
    url = 'http://api.openweathermap.org/data/2.5/box/city?appid=e229425a7ad4dc9b361f341f7ce03904'

    payload = {
        "bbox": "12.3,36.8,15.58,38.26,10", #rectangle of sicily long_left,lat_bottom_long_right_lat_top,zoom
    }
    # GET with params in URL
    r = requests.get(url, params=payload)
    c=r.json()

    lon=[]
    lat=[]
    t=[]
    id=[]
    temp_max=[]
    pressure=[]
    temp=[]
    humidity=[]
    temp_min=[]
    name=[]
    wind_deg=[]
    wind_speed=[]

    for i in range(0,len(c["list"])-1):
        lon.append(c["list"][i]["coord"]["Lon"])
        lat.append(c["list"][i]["coord"]["Lat"])
        id.append(c["list"][i]["id"])
        temp_max.append(c["list"][i]["main"]["temp_max"])
        pressure.append(c["list"][i]["main"]["pressure"])
        temp.append(c["list"][i]["main"]["temp"])
        humidity.append(c["list"][i]["main"]["humidity"])
        temp_min.append(c["list"][i]["main"]["temp_min"])
        name.append(c["list"][i]["name"])
        wind_deg.append(c["list"][i]["wind"]["deg"])
        wind_speed.append(c["list"][i]["wind"]["speed"])
        x_t=c["list"][i]["dt"]
        t.append((datetime.datetime.fromtimestamp(x_t)).ctime())
        #year.append(t.year)
        #months=t.month
        #day=t.day
        #hour=t.hour
        #minutes=t.minute
        #seconds=t.second
    return name, lon, lat,pressure, temp, humidity,wind_speed,t



#create_station()
#delete_stations()


#post_value()
name, lon, lat,pressure, temp, humidity,wind_speed,t=get_value_from_rectangle()
owm_beta1.visual(name, lon, lat,pressure, temp, humidity,wind_speed,t)
#get_stations()




