
from bokeh.plotting import show
from bokeh.models import (
    GMapPlot, Range1d,
    PanTool, WheelZoomTool, GMapOptions, HoverTool, SquareX, ColumnDataSource, Circle, DataRange1d)


def visual(name, lon, lat,pressure, temp, humidity,wind_speed):
    map_options = GMapOptions(lat=37, lng=14.3612, zoom=8)

    hover = HoverTool(

            tooltips=[
                ("name station", "@name"), #$variabili specifiche @variabili presenti nel source columnData
                ("long","@lon"),
                ("lat","@lat"),
                ("Wind speed", "@wind_speed"),
                ("Temperature", "@temp"),
                ("Humidity", "@humidity")

            ]
        )

    plot = GMapPlot(
        x_range=DataRange1d(),
        y_range=DataRange1d(),
        plot_width=1000,
        plot_height=700,
        map_options=map_options,
        webgl=True,
        api_key="AIzaSyCs3DbjLI4ruaQAcZSrZqA52xbHfMrblo8",

    )





    source = ColumnDataSource(
        data=dict(
            lat=lat,
            lon=lon,
            name=name,
            temp=temp,
            humidity=humidity,
            wind_speed=wind_speed

        )
    )
    #pan = PanTool()
    #wheel_zoom = WheelZoomTool()
    #circle = Circle(x=13.3612,y=13.3612,size=250, line_color='blue', fill_color='blue', fill_alpha=0.4)
    circle= Circle(x="lon", y="lat", size=50, line_color='blue', fill_color='blue', fill_alpha=0.5)
    plot.add_glyph(source,circle)
    plot.add_tools(hover)
    show(plot)
