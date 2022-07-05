import folium
import pandas as pd

vol = pd.read_csv("./Volcanoes.txt", delimiter=",")

map = folium.Map(location=[38.58, -110], zoom_start= 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

lat = list(vol["LAT"])
lon = list(vol["LON"])
name = list(vol["NAME"])
stat = list(vol["STATUS"])

statuses = pd.unique(stat) #unique statuses fount in the "STATUS" column of the valcanoe dataframe

#generates colour for the volcanoe marker based on the stsus provided in the volcanoe.txt
def color_gen(status):
    if status == "Historical":
        return "purple"
    elif status == "Tephrochronology":
        return "orange"
    elif status == "Dendrochronology":
        return "darkred"
    elif status == "Radiocarbon":
        return "pink"
    elif status == "Varve Count":
        return "gray"
    elif status == "Holocene?":
        return "lightgreen"
    elif status == "Holocene":
        return "green"
    elif status == "Pleistocene-Fumarolic":
        return "darkblue"
    elif status == "Anthropology":
        return "cadetblue"
    else:
        return "white"

#pop-up uses name of volcanoe instead of name of elev in the original course
for i, j, n, st in zip(lat, lon, name, stat):
    color = color_gen(st)
    fg.add_child(folium.Marker(location=[i, j], popup = n, icon=folium.Icon(color = color)))

    
    
map.add_child(fg)

map.save("Map.html")
