from flask import Flask
import folium
import geopandas as gpd

gdf = gpd.read_file("../data/processed/gdf_w_clusters.shp")

app = Flask(__name__)


@app.route('/')
def index():
    folium_map = gdf.explore(column = 'rel_probs', cmap='seismic', legend_kwds = {'caption': 'Realtive Probability'}\
                            prefer_canvas = True)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)