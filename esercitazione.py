import urllib

from bokeh.plotting import show
import xml.etree.ElementTree as ET
from bokeh.models import (
    GMapPlot, Range1d,
    PanTool, WheelZoomTool, GMapOptions, HoverTool, SquareX, ColumnDataSource, Circle, DataRange1d)



map_options = GMapOptions(lat=38.1156879, lng=13.3612, zoom=15)

hover = HoverTool(

        tooltips=[
            ("index", "$index"), #$variabili specifiche @variabili presenti nel source columnData
            ("long","@lon"),
            ("lat","@lat")
        ]
    )

plot = GMapPlot(
    x_range=DataRange1d(),
    y_range=DataRange1d(),
    height=700,
    width=700,
    map_options=map_options,
    webgl=True,
    api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqA52xbHfMrblo8",

)

latitude=[]
longitude=[]
tree =ET.parse(urllib.request.urlopen('https://www.comune.palermo.it/xmls/VIS_DATASET_TURISMO03.xml'))
root = tree.getroot()
for i in root.findall('DATA_RECORD'):
    #print(i.find('LATITUDE').text, i.find('LONGITUDE').text)
    latitude.append(float(i.find('LATITUDE').text.replace(',','.')))
    longitude.append(float(i.find('LONGITUDE').text.replace(',','.')))

source = ColumnDataSource(
    data=dict(
        lat=latitude,
        lon=longitude,
    )
)
#pan = PanTool()
#wheel_zoom = WheelZoomTool()
#circle = Circle(x=13.3612,y=38.1156879,size=250, line_color='blue', fill_color='blue', fill_alpha=0.4)
circle= Circle(x="lon", y="lat", size=20, line_color='blue', fill_color='blue', fill_alpha=0.4)
plot.add_glyph(source,circle)
plot.add_tools(hover)
show(plot)
