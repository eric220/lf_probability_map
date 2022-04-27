from flask import Flask
import geopandas as gpd
import folium

app = Flask(__name__)
gdf = gpd.read_file("../deploy_data/gdf_w_clusters.shp")

@app.route('/')
def home():
    folium_map = explore_df.explore(column = 'rel_probs', cmap='seismic', legend_kwds = {'caption': 'Realtive Probability'},\
                   prefer_canvas = True)
    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)