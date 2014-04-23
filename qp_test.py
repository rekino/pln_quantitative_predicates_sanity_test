import csv
from numpy.ma import mean
import numpy
from sklearn.cluster import KMeans
from data.data_container import DataContainer3DCsv

__author__ = 'ramin'

dc = DataContainer3DCsv()

sorted_gdps = sorted([country['gdp'] for country in dc.values()])

bins = [[] for t in xrange(10)]
i = 0
j = -1

for gdp in sorted_gdps:
    if i % 19 == 0:
        j += 1
    bins[j].append(gdp)
    i += 1

writer = csv.writer(open('clusters_gdp.csv', 'w'))
for bin in bins:
    m = mean(bin)
    Min = min(bin)
    Max = max(bin)
    writer.writerow((Min, m, Max))
