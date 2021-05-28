import folium
import pandas

base_map=folium.Map(location=[38.89,105.89],zoom_start=2,tiles="Stamen Terrain")
data=pandas.read_csv("Volcanoes.txt")
color=""
list_lat=list(data["LAT"])
list_lon=list(data["LON"])
list_elev=list(data["ELEV"])
list_name=list(data["NAME"])
for lat,lon,elev,name in zip(list_lat,list_lon,list_elev,list_name):
    if elev > 3500:
        color="red"
    elif elev > 2000:
        color="green"
    else:
        color="gray"
    base_map=base_map.add_child(folium.CircleMarker(location=[lat,lon],radius=6,popup=f"{name}\n{str(elev)}m",fill_color=color,color="black",fill=True,fill_opacity=0.7))
base_map=base_map.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read()))
base_map=base_map.save("display.html")