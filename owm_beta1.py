
from bokeh.plotting import show
from bokeh.models import (
    GMapPlot, Range1d,
    PanTool, WheelZoomTool, GMapOptions, HoverTool, SquareX, ColumnDataSource, Circle, DataRange1d, String)


def visual(name, lon, lat,pressure, temp, humidity,wind_speed,t):



    map_options = GMapOptions(lat=37.6, lng=13.6, zoom=9)

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
        x_range=DataRange1d(),
        y_range=DataRange1d(),
        plot_width=1300,
        plot_height=800,
        map_options=map_options,
        webgl=True,
        api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqA52xbHfMrblo8",

    )


    #create an heatmap
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
    #pan = PanTool()
    #wheel_zoom = WheelZoomTool()
    #circle = Circle(x=13.3612,y=13.3612,size=250, line_color='blue', fill_color='blue', fill_alpha=0.4)
    circle= Circle(x="lon", y="lat", size=50, line_color='blue', fill_color="color", fill_alpha=0.5)
    plot.add_glyph(source,circle)
    plot.add_tools(hover)
    show(plot)
