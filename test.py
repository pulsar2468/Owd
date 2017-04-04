import folium


def visual(name, lon, lat,pressure, temp, humidity,wind_speed,t):
    map_1 = folium.Map(location=[37.57, 13.92], zoom_start=8,tiles='stamenwatercolor')
    #folium.Marker([37.57, 13.92], popup='Mt. Hood Meadows').add_to(map_1)
    #folium.Marker([37.57, 13.92], popup='Timberline Lodge').add_to(map_1)
    feature_group = folium.FeatureGroup("Locations")
    color=[]
    for lat, lng, name,i_temp in zip(lat, lon, name,temp):
        if i_temp < 14:
            color="blue"
        else:
            color="red"

        feature_group.add_child(folium.CircleMarker(location=[lat, lng],radius=30, popup=name,fill_color=color))

    map_1.add_child(feature_group)
    map_1.save("mthood.html")