import folium
import pandas as pd

vol = pd.read_csv("./Volcanoes.txt", delimiter=",")

map = folium.Map(location=[38.58, -110], zoom_start= 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

lat = list(vol["LAT"])
lon = list(vol["LON"])
name = list(vol["NAME"])

for i, j, k in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[i, j], popup = k, icon=folium.Icon(color = "darkred")))
    
    
map.add_child(fg)

map.save("Map.html")
