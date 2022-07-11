import folium
from out import venue_locations
import webbrowser
from folium.plugins import FastMarkerCluster

if __name__ == "__main__":
    latitudes_uhh = [i[0] for i in venue_locations.coords_uhh]
    longitudes_uhh = [i[1] for i in venue_locations.coords_uhh]
    latitudes_tuhh = [i[0] for i in venue_locations.coords_tuhh]
    longitudes_tuhh = [i[1] for i in venue_locations.coords_tuhh]
    latitudes_haw = [i[0] for i in venue_locations.coords_haw]
    longitudes_haw = [i[1] for i in venue_locations.coords_haw]
    folium_map = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')
    uhh_layer = folium.FeatureGroup(name="University of Hamburg")
    uhh_cluster = FastMarkerCluster(data=list(zip(latitudes_uhh, longitudes_uhh))).add_to(uhh_layer)
    tuhh_layer = folium.FeatureGroup(name="Hamburg University of Technology")
    tuhh_cluster = FastMarkerCluster(data=list(zip(latitudes_tuhh, longitudes_tuhh))).add_to(tuhh_layer)
    haw_layer = folium.FeatureGroup(name="Hamburg University of Applied Sciences")
    haw_cluster = FastMarkerCluster(data=list(zip(latitudes_haw, longitudes_haw))).add_to(haw_layer)
    folium_map.add_child(uhh_layer)
    folium_map.add_child(tuhh_layer)
    folium_map.add_child(haw_layer)
    folium_map.add_child(haw_layer)
    folium_map.add_child(folium.map.LayerControl())
    folium_map.save("map.html")
    webbrowser.open("map.html")