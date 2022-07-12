import folium
from out import venue_locations
import webbrowser
from folium.plugins import MarkerCluster, HeatMap

if __name__ == "__main__":
    latitudes_uhh = [i[0] for i in venue_locations.uhh_coords]
    longitudes_uhh = [i[1] for i in venue_locations.uhh_coords]
    latitudes_tuhh = [i[0] for i in venue_locations.tuhh_coords]
    longitudes_tuhh = [i[1] for i in venue_locations.tuhh_coords]
    latitudes_haw = [i[0] for i in venue_locations.haw_coords]
    longitudes_haw = [i[1] for i in venue_locations.haw_coords]
    folium_map = folium.Map(location=[20, 0], max_bounds=True, zoom_start=2, tiles='CartoDB positron')
    uhh_layer = folium.FeatureGroup(name="University of Hamburg")
    uhh_cluster = MarkerCluster(locations=list(zip(latitudes_uhh, longitudes_uhh)), popups=venue_locations.uhh_ven).add_to(uhh_layer)
    HeatMap(venue_locations.uhh_coords).add_to(uhh_layer)
    tuhh_layer = folium.FeatureGroup(name="Hamburg University of Technology")
    tuhh_cluster = MarkerCluster(locations=list(zip(latitudes_tuhh, longitudes_tuhh)), popups=venue_locations.tuhh_ven).add_to(tuhh_layer)
    HeatMap(venue_locations.tuhh_coords).add_to(tuhh_layer)
    haw_layer = folium.FeatureGroup(name="Hamburg University of Applied Sciences")
    haw_cluster = MarkerCluster(locations=list(zip(latitudes_haw, longitudes_haw)), popups=venue_locations.haw_ven).add_to(haw_layer)
    HeatMap(venue_locations.haw_coords).add_to(haw_layer)
    folium_map.add_child(uhh_layer)
    folium_map.add_child(tuhh_layer)
    folium_map.add_child(haw_layer)
    folium_map.add_child(haw_layer)
    folium_map.add_child(folium.map.LayerControl())
    folium_map.save("map.html")
    webbrowser.open("map.html")
