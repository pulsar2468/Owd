import folium
import owm_test

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

