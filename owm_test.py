import datetime
import requests
import time


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
        "latitude": 37.76,
        "longitude": -122.43,
        "altitude": 20
    }

    #headers = {'Content-Type': 'application/json'}

    # GET with params in URL
    r = requests.post(url, json=payload)
    print(r.status_code,r.text)



#create_station()
#delete_stations()


#post_value()
get_value()
#get_stations()
#
