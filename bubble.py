import requests
from geopy import Nominatim
import datetime
import time


def get_forecast():
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?&appid=e229425a7ad4dc9b361f341f7ce03904'

    payload = {
        "q": "Palermo",
        "type": "accurate",
        "units":"metric",
        "cnt": 10,
    }
    # GET with params in URL
    r = requests.get(url,params=payload)
    c = r.json()

    lon = []
    lat = []
    t = []
    id = []
    temp_max = []
    pressure = []
    temp = []
    humidity = []
    temp_min = []
    name = []
    wind_deg = []
    wind_speed = []
    for i in range(0, len(c["list"])):
        #lon.append(c["list"][i]["coord"]["Lon"])
        #lat.append(c["list"][i]["coord"]["Lat"])
        #id.append(c["list"][i]["id"])
        temp_max.append(c["list"][i]["temp"]["max"])
        #pressure.append(c["list"][i]["main"]["pressure"])
        #temp.append(c["list"][i]["main"]["temp"])
        #humidity.append(c["list"][i]["main"]["humidity"])
        #temp_min.append(c["list"][i]["main"]["temp_min"])
        #name.append(c["list"][i]["name"])
        #wind_deg.append(c["list"][i]["wind"]["deg"])
        #wind_speed.append(c["list"][i]["wind"]["speed"])
        x_t = c["list"][i]["dt"]
        t.append((datetime.datetime.fromtimestamp(x_t)).ctime())
        # year.append(t.year)
        # months=t.month
        # day=t.day
        # hour=t.hour
        # minutes=t.minute
        # seconds=t.second
    return t,temp_max



def name_station():
    geolocator = Nominatim()
    location = geolocator.geocode("Sicily")  # i get the center of city/region espress to lat/lon
    url = 'http://api.openweathermap.org/data/2.5/station/find?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&cnt=3&appid=e229425a7ad4dc9b361f341f7ce03904'
    #bbox = str(location.longitude - 2) + ',' + str(location.latitude - 2) + ',' + str(
        #location.longitude + 2) + ',' + str(location.latitude + 2) + ',' + str(10)
    #payload = {
        #"bbox": bbox,  # +-1 on coordinates, it's will move me for 111km in both directions
        #"cnt": 1,
    #}
    # GET with params in URL
    r = requests.get(url)
    print(r.text)
    '''
    c = r.json()
    lon = []
    lat = []
    t = []
    id = []
    temp_max = []
    pressure = []
    temp = []
    humidity = []
    temp_min = []
    name = []
    wind_deg = []
    wind_speed = []
    for i in range(0, len(c["list"])):
        # lon.append(c["list"][i]["coord"]["Lon"])
        # lat.append(c["list"][i]["coord"]["Lat"])
        # id.append(c["list"][i]["id"])
        temp_max.append(c["list"][i]["temp"]["max"])
        # pressure.append(c["list"][i]["main"]["pressure"])
        # temp.append(c["list"][i]["main"]["temp"])
        # humidity.append(c["list"][i]["main"]["humidity"])
        # temp_min.append(c["list"][i]["main"]["temp_min"])
        # name.append(c["list"][i]["name"])
        # wind_deg.append(c["list"][i]["wind"]["deg"])
        # wind_speed.append(c["list"][i]["wind"]["speed"])
        x_t = c["list"][i]["dt"]
        t.append((datetime.datetime.fromtimestamp(x_t)).ctime())
        # year.append(t.year)
        # months=t.month
        # day=t.day
        # hour=t.hour
        # minutes=t.minute
        # seconds=t.second
    return t, temp_max
    '''



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


#t,temp=get_forecast()
name_station()
get_value()
#print(t,temp)