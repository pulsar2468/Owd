import json
import locale

import folium
import sqlite3
import datetime

from bokeh.palettes import mpl
from bokeh.models import VBox, ColumnDataSource, TableColumn, DataTable, DateFormatter, NumberFormatter, BoxAnnotation, \
    Button, PreText
from bokeh.plotting import figure
import owm_test
from bokeh.resources import CDN
from bokeh.embed import file_html


def visual(name, lon, lat, pressure, temp, humidity, wind_speed, t,id):
    map_1 = folium.Map(location=[37.57, 13.92], zoom_start=8, tiles='stamenwatercolor')
    feature_group = folium.FeatureGroup("Locations")

    for lat, lng, name, i_temp,time,h,wind in zip(lat, lon, name, temp,t,humidity,wind_speed):
        if i_temp < 14:
            color = "blue"
        else:
            color = "red"

        html = '<font face="Verdana" size="2" color="red">'  \
               'Ws: %s<br>' \
               'Lat: %s<br>' \
               'Lon: %s<br>' \
               'Temp: %s<br>' \
               'Detection_Time: %s<br>' \
               'Humidity: %f<br>' \
               'Wind_speed: %f</font>' \
               %(name,lat,lng,i_temp,time,h,wind)
        frame_html = folium.Html(html, script=True, width=120, height=200)
        popup = folium.Popup(frame_html)

        feature_group.add_child(folium.CircleMarker(location=[lat, lng], radius=30, popup=popup, fill_color=color))

    map_1.add_child(feature_group)
    map_1.save("real_timeMap.html")


def real_time():
    name, lon, lat, pressure, temp, humidity, wind_speed, t, id = owm_test.get_value_from_rectangle()
    visual(name, lon, lat, pressure, temp, humidity, wind_speed, t, id)


def on_click(data):
    print('Cvs: ',data)



def schema(response):
    temp = []
    dT = []
    wind=[]
    hum=[]
    latest_list = []
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT City.id,''"%s".name,"%s".detection_time,' \
          'City.lat,City.lon,"%s".temp,"%s".humidity,"%s".wind_speed ' \
          'FROM "%s",City WHERE City.name="%s".name' % (
          response, response, response, response, response, response, response)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()

    for i in range(0, len(latest_list)):
        dT.append(datetime.datetime.strptime(latest_list[i][2], "%a %b %d %H:%M:%S %Y"))
        temp.append(latest_list[i][5])
        hum.append(latest_list[i][6])
        wind.append(latest_list[i][7])

    #Plot 1
    p1 = figure(width=800, height=300, tools='pan,box_zoom,reset',x_axis_type="datetime")
    p1.line(dT,temp)
    p1.title = "Temperature"
    p1.xaxis.axis_label = 'Time'
    p1.yaxis.axis_label = 'Value'
    low_box = BoxAnnotation(plot=p1, top=15, fill_alpha=0.4, fill_color='#084594')
    mid_box = BoxAnnotation(plot=p1, bottom=15, top=23, fill_alpha=0.4, fill_color='#FBA40A')
    high_box = BoxAnnotation(plot=p1, bottom=23, fill_alpha=0.5, fill_color='red')
    p1.renderers.extend([low_box,mid_box, high_box])
    p1.logo=None




    p2 = figure(width=800, height=300, tools='pan,box_zoom,reset',x_axis_type="datetime")
    p2.line(dT,hum)
    p2.title = "Humidity"
    p2.xaxis.axis_label = 'Time'
    p2.yaxis.axis_label = 'Value'
    p2.logo=None



    p3 = figure(width=800, height=300, tools='pan,box_zoom,reset', x_axis_type="datetime")
    p3.line(dT, wind)
    p3.title = "Wind Speed"
    p3.xaxis.axis_label = 'Time'
    p3.yaxis.axis_label = 'Value'
    p3.logo=None



    p4 = figure(width=800, height=300, tools='pan,box_zoom,reset', x_axis_type="datetime")
    p4.multi_line([dT,dT,dT], [temp,hum,wind],line_color=['#0C0786', '#CA4678', '#EFF821'])
    p4.title = "All"
    p4.xaxis.axis_label = 'Time'
    p4.yaxis.axis_label = 'Value'
    p4.logo=None
    p4.legend.location = "top_left"
    p4.legend.click_policy = "hide"



    #Creation dataTable of history city
    data = dict(
        dates=[i.ctime() for i in dT],
        temperature=temp,
        humidity=hum,
        wind=wind
    )
    source = ColumnDataSource(data)

    columns = [
        TableColumn(field="dates", title="Date", width=300),
        TableColumn(field="temperature", title="Temperature"),
        TableColumn(field="humidity", title="Humidity"),
        TableColumn(field="wind", title="Wind_speed m/s")
    ]
    data_table = DataTable(source=source, columns=columns, width=800, height=280)

    #button = Button(label="Download it!", button_type="success",clicks=on_click(latest_list))
    pre = PreText(text=(json.dumps({'results': latest_list})), width=800, height=1000)

    p=VBox(p1,p2,p4,data_table,pre)
    html=file_html(p,CDN)
    return html

