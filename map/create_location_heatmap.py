import folium
from out import venue_locations
import webbrowser
from folium.plugins import FastMarkerCluster, HeatMap, MarkerCluster

if __name__ == "__main__":
    folium_map = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')

    uhh_layer = folium.FeatureGroup(name="University of Hamburg")
    HeatMap(venue_locations.uhh_coords).add_to(uhh_layer)
    folium_map.add_child(uhh_layer)

    tuhh_layer = folium.FeatureGroup(name="Hamburg University of Technology")
    HeatMap(venue_locations.tuhh_coords).add_to(tuhh_layer)
    folium_map.add_child(tuhh_layer)

    haw_layer = folium.FeatureGroup(name="Hamburg University of Applied Sciences")
    HeatMap(venue_locations.haw_coords).add_to(haw_layer)
    folium_map.add_child(haw_layer)

    folium_map.add_child(folium.map.LayerControl())

    folium_map.save("map_hm.html")
    webbrowser.open("map_hm.html")
