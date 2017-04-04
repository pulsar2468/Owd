from bokeh.plotting import show
from bokeh.models import (
    GMapPlot, Range1d,
    PanTool, WheelZoomTool, GMapOptions, HoverTool, ColumnDataSource, Circle, DataRange1d, ResetTool, SaveTool, String)


def visual(name, lon, lat,pressure, temp, humidity,wind_speed,t):


    x_range=Range1d()
    y_range=Range1d()
    map_options = GMapOptions(lat=37.57, lng=13.92, zoom=8 ,map_type='satellite')

    hover = HoverTool(

            tooltips=[
                ("name station", "@name"), #$variabili specifiche @variabili presenti nel source columnData
                ("long","@lon"),
                ("lat","@lat"),
                ("Wind speed", "@wind_speed"),
                ("Temperature", "@temp"),
                ("Humidity", "@humidity"),
                ("Detection Time", "@t")

            ]
        )

    plot = GMapPlot(
        x_range=x_range,
        y_range=y_range,
        map_options=map_options,
        #webgl=True,
        api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqqA52xbHfMrblo8",

    )
    plot.title.text="Weather"


    #create a colors of markers
    color=[]
    for i in temp:
        if i < 12:
            color.append("blue")
        else:
            color.append("red")

    source = ColumnDataSource(
        data=dict(
            lat=lat,
            lon=lon,
            name=name,
            temp=temp,
            humidity=humidity,
            wind_speed=wind_speed,
            t=t,
            color=color

        )
    )
    pan = PanTool()
    wheel_zoom = WheelZoomTool()
    reset= ResetTool()
    save= SaveTool()
    #circle = Circle(x=13.3612,y=13.3612,size=250, line_color='blue', fill_color='blue', fill_alpha=0.4)
    circle= Circle(x="lon", y="lat", radius=10, line_color='blue', fill_color="color", fill_alpha=0.5)
    plot.add_glyph(source,circle)
    plot.add_tools(hover,pan,wheel_zoom,reset,save)
    #plot.legend.location = "bottom_right"
    #plot.legend.background_fill_color = "navy"
    #plot.legend.background_fill_alpha = 0.5
    show(plot)
