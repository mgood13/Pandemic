"""
Annotate on hover
=================

When ``hover`` is set to ``True``, annotations are displayed when the mouse
hovers over the artist, without the need for clicking.
"""

import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import csv
import networkx as nx
np.random.seed(42)
colors = ['blue', 'yellow', 'red', 'black']
color_dict = {'blue': 0, 'yellow': 0, 'red': 0, 'black': 0}


f = open('Pandemic Locations.csv', encoding='utf-8-sig')
city_dictionary = {}
count = 0

with f:
    reader = csv.reader(f)
    for row in reader:
        city_dictionary[row[1]] = {'Color': row[0], 'Latitude': row[2], 'Longitude': row[3],
                                   'Population': row[4], 'X': row[5], 'Y': row[6], 'ID': row[7], 'Connections': row[8],
                                   'Disease State': color_dict}
    f.close()


cities = list(city_dictionary.keys())
x = {'blue': [], 'yellow': [], 'red': [], 'black': []}
y = {'blue': [], 'yellow': [], 'red': [], 'black': []}
xmapped = []
ymapped = []
names = np.array(cities[0:24])



for city in cities:
    if city_dictionary[city]['Color'] == 'blue':
        x['blue'].append(float(city_dictionary[city]['Longitude']))
        y['blue'].append(float(city_dictionary[city]['Latitude']))
        xmapped.append(float(city_dictionary[city]['X']))
        ymapped.append(float(city_dictionary[city]['Y']))
    if city_dictionary[city]['Color'] == 'yellow':
        x['yellow'].append(float(city_dictionary[city]['Longitude']))
        y['yellow'].append(float(city_dictionary[city]['Latitude']))
        xmapped.append(float(city_dictionary[city]['X']))
        ymapped.append(float(city_dictionary[city]['Y']))
    if city_dictionary[city]['Color'] == 'red':
        x['red'].append(float(city_dictionary[city]['Longitude']))
        y['red'].append(float(city_dictionary[city]['Latitude']))
    if city_dictionary[city]['Color'] == 'black':
        x['black'].append(float(city_dictionary[city]['Longitude']))
        y['black'].append(float(city_dictionary[city]['Latitude']))

plt.style.use('dark_background')

cmap = plt.cm.RdYlGn
norm = plt.Normalize(1,4)

img = plt.imread("BlackMarble_2016_01deg.jpg")
fig, ax = plt.subplots(figsize=(16,6))
ax.imshow(img, extent=[0, 200, 0, 100])
ax.set_title('WELCOME TO PANDEMIC. OR... THE REAL WORLD')

#for color in x:
#    plt.scatter(x[color], y[color], s=2, c=color)

categories = np.array([])
for i in xmapped:
    if count < 12:
        categories = np.append(categories, [0])
    else:
        categories = np.append(categories, [1])
        print("hi")
    count += 1
print(categories.dtype)
categories = categories.astype(int)
print(categories.dtype)

colormap = np.array(['blue', 'yellow'])

#plt.scatter(a[0], a[1], s=100, c=colormap[categories])


sc = plt.scatter(xmapped[0:24], ymapped[0:24], s=10, c=colormap[categories])
#sc1 = plt.scatter(xmapped[13:24], ymapped[13:24], s=10, c='yellow')

annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="b"),
                    arrowprops=dict(arrowstyle="-"))
annot.set_visible(False)

def update_annot(ind):
    print(ind)
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos

    #text = "{}\n{}".format(" ".join(str(pos)), " ".join([names[n] for n in ind["ind"]]))
    text = "{}\n{}\n{}".format(" ".join([names[n] for n in ind["ind"]]), "Diseases Present: EBOLA", "Concern Level: Normal")
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor('black')
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        # this line checks if the position of the mouse equals one of the scatter points
        # cont becomes true if it is
        cont, ind = sc.contains(event)
        print(cont)
        print("THis is ind:    ")
        print(ind)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

#def diseasecubes():
    # Store all of the disease cube states

#def concernlevel():
# Define a value for how close a city is to outbreaking and change... color or size

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.axis('off')
plt.show()

#xtest = x['blue'][0:2]
#ytest = y['blue'][0:2]
#plt.plot(xtest,ytest,)
#print(xtest)
#plt.subplots_adjust(left=0.13, bottom=0.04, right=0.90, top=0.96, wspace=0.07, hspace=0.08)
#mplcursors.cursor(hover=True)
#fig, ax = plt.subplots()
#x = [1,2]
#y = [3,4]
#ax.scatter(x,y)
#ax.set_title("Mouse over a point")
#plt.show()
#count = 0
#G = nx.Graph()
#for value in city_dictionary:
#    G.add_node(value,pos = (float(city_dictionary[cities[count]]['Longitude']), float(city_dictionary[cities[count]]['Latitude'])))
#    count += 1
#    nx.draw(G)
    #print(pos)
#pos = G.get_node_attribute(G,'pos')
#nx.draw(G,pos)

#for city in cities:
#    G.add_node()
#G.add_nodes_from()
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()

 
