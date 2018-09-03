import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as Poly
from matplotlib.collections import PatchCollection
from ellipse import Ellipse
from ellipse import find_distance_for_half_intersect

##############################################################
#THIS SECTION IN CONFIGURABLE ################################
##############################################################
VERTICAL_AXE_REFERENCE = 1
HORIZONTAL_AXE_REFERENCE = 1
VERTICAL_AXE_INTERSECT = 1
HORIZONTAL_AXE_INTERSECT = 1
##############################################################
#END OF CONFIGURABLE SECTION #################################
##############################################################


elo_1 = Ellipse(HORIZONTAL_AXE_REFERENCE, VERTICAL_AXE_REFERENCE)
elo_2 = Ellipse(HORIZONTAL_AXE_INTERSECT, VERTICAL_AXE_INTERSECT)

find_distance_for_half_intersect(elo_1, elo_2)


x,y = elo_1.polygon.exterior.xy
i,j = elo_2.polygon.exterior.xy
k,l = elo_1.intersection(elo_2).exterior.xy


fig, ax = plt.subplots()
polygons = []
num_polygons = 2
num_sides = 5


polygon = Poly(zip(x,y), True)
polygons.append(polygon)
polygon = Poly(zip(i,j), True)
polygons.append(polygon)
polygon = Poly(zip(k,l), True)
polygons.append(polygon)

p = PatchCollection(polygons, cmap=matplotlib.cm.jet, alpha=0.4)

colors = 100*np.random.rand(len(polygons))
p.set_array(np.array(colors))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.add_collection(p)
lim = max(elo_2.b, elo_2.a)
plt.ylim((-2*lim,2*lim))
plt.xlim((-2*lim,2*lim))
plt.show()