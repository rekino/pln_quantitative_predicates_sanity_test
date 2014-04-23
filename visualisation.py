import numpy
import csv
from scipy.stats import pearsonr
from sklearn.cluster import KMeans
from data.data_container import DataContainer3DCsv

__author__ = 'Ramin'

dc = DataContainer3DCsv()
# print dc.max(), dc.max('areas'), dc.max('populations')
# dc.plot()
# dc.plot_1D(ax='areas')
# dc.plot_2D(ax_1='gdps', ax_2='populations')

estimator = KMeans(10)
data = dc.zip()
estimator.fit(data)

clusters = {}

for key in dc:
    point = dc.get_data_of(key)
    [label] = estimator.predict(point)
    dc[key]['label'] = label
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(point)

clusters_country = {}
for country in dc:
    label = dc[country]['label']
    if label not in clusters_country:
        clusters_country[label] = []
    clusters_country[label].append(country)

writer = csv.writer(open('clusters_3D.csv', 'w'))
for key, value in clusters_country.items():
    writer.writerow(value)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cpool = [ '#bd2309', '#bbb12d', '#1480fa', '#14fa2f', '#000000',
              '#faf214', '#2edfea', '#ea2ec4', '#ea2e40', '#cdcdcd',
              '#577a4d', '#2e46c0', '#f59422', '#219774', '#8086d9' ]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, label in enumerate(clusters):
    clusters[label] = numpy.array(clusters[label])
    cluster = clusters[label]
    ax.scatter(cluster[:, 0], cluster[:, 1], cluster[:, 2], c=cpool[i])

ax.set_xlabel('GDP')
ax.set_ylabel('Area')
ax.set_zlabel('Population')

plt.show()

