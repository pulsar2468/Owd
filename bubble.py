import folium
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Palermo")


html = '<h1> This is a big popup</h1><br>'
frame_html = folium.Html(html,script=True,width=100,height=300)
popup = folium.Popup(frame_html, max_width=2650)
map_1 = folium.Map(location=[37.57, 13.92], zoom_start=8,tiles='stamenwatercolor')
map_1.add_child(folium.CircleMarker(location=[37.57, 13.92], radius=30, popup=popup,fill_color="blue"))
map_1.save("mthood.html")