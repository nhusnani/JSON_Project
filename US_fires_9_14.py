import json

infile = open('US_fires_9_14.json', 'r')
outfile = open('readable_US_fires_9_14.json','w')

# The json.load() function converts the data into a format Python
# can work with: in this case, a giant dictionary.
fires_data = json.load(infile)

json.dump(fires_data, outfile, indent = 4)

lats, lons, brightness = [],[],[]

for fire in fires_data:
    if int(fire["brightness"]) > 450:
        lat = fire['latitude']
        lon = fire['longitude']
        bright = int(fire['brightness'])
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)

print(lats[:10])
print(lons[:10])
print(brightness[:10])


from plotly.graph_objs import Scattergeo, Layout # Scattergeo allows to use scatter points and plot on a map
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        #'size': [5 * mag for mag in mags],
        'color': brightness,
        'colorscale':'viridis',
        'reversescale': True,
        'colorbar': {"title":"Brightness"}
    }
}]

my_layout = Layout(title='California Fire - 9-14-20 to 9-20-20')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='california_fire_9_14.html')