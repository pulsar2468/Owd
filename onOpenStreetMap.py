import folium


def visual(name, lon, lat, pressure, temp, humidity, wind_speed, t):
    map_1 = folium.Map(location=[37.57, 13.92], zoom_start=8, tiles='stamenwatercolor')
    feature_group = folium.FeatureGroup("Locations")

    for lat, lng, name, i_temp in zip(lat, lon, name, temp):
        if i_temp < 14:
            color = "blue"
        else:
            color = "red"

        html = '<font face="Verdana" size="3" color="red">'  \
               '<p>%s</p>' \
               '<p>%s</p>' \
               '<p>%s</p>' \
               '<p>%s</p></font>'%(name,lat,lng,i_temp)
        frame_html = folium.Html(html, script=True, width=50, height=100)
        popup = folium.Popup(frame_html)

        feature_group.add_child(folium.CircleMarker(location=[lat, lng], radius=30, popup=popup, fill_color=color))

    map_1.add_child(feature_group)
    map_1.save("mthood.html")
