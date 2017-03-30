'''
import random


def bubble():
    n = len(a)

    while True:
        k = 0;
        for i in range(0, n - 1):

            if a[i] > a[i + 1]:
                aus = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aus
                k = 1
        if k == 0:
            break;

        --n;


a = [random.randint(0, 10) for i in range(1, 10)]
print(a)
bubble()
print(a)

import gmaps
import gmaps.datasets

gmaps.configure(api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqA52xbHfMrblo8")  # Your Google API key

import gmplot

gmap = gmplot.GoogleMapPlotter(38.1156879, 13.3612, 16)

# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
gmap.marker(38.1156879, 13.3612, "yellow")
#path4 = [(37.753074,37.746700),(-122.43,-122.439)]
#gmap.heatmap(path4[0], path4[1], threshold=50, radius=100)
gmap.circle(38.1156879, 13.3612, 200, "blue")
#gmap.grid(37.42, 37.43, 0.001, -122.15, -122.14, 0.001) crea una griglia
#gmap.polygon(path4[0], path4[1], edge_color="cyan", edge_width=5, face_color="blue", face_alpha=0.1) stessa cosa di sotto
#gmap.plot(path4[0], path4[1], "red") linea che collega coppie di punti heat
gmap.draw("mymap1.html")
'''


from bokeh.plotting import show

from bokeh.models.glyphs import Circle
from bokeh.models import (
    GMapPlot, Range1d,
    PanTool, WheelZoomTool, GMapOptions, HoverTool)


x_range = Range1d(-160, 160)
y_range = Range1d(-80, 80)

map_options = GMapOptions(lat=38.1156879, lng=13.3612, zoom=15)

hover = HoverTool(

        tooltips=[
            ("index", "$index"),
            ("Temperature","($temp_rand)")
        ]
    )

plot = GMapPlot(
    x_range=x_range,
    y_range=y_range,
    plot_width=1000,
    plot_height=500,
    map_options=map_options,
    webgl=True,
    api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqA52xbHfMrblo8",


)

pan = PanTool()
wheel_zoom = WheelZoomTool()
path4 = [(37.753074,37.746700),(-122.43,-122.439)]
circle = Circle(x=13.3612,y=38.1156879,size=250, line_color='blue', fill_color='blue', fill_alpha=0.4)
plot.add_glyph(circle)
plot.add_tools(pan, wheel_zoom,hover)
show(plot)