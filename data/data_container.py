import csv
from mpl_toolkits.mplot3d import Axes3D
from numpy import mean, std
import matplotlib.pyplot as plt
import numpy

__author__ = 'ramin'


class DataContainer(dict):
    def plot(self):
        pass


class DataContainer3DCsv(DataContainer):
    def __init__(self):
        gdp_reader = csv.reader(open('data/gdp.csv', 'r'))
        area_reader = csv.reader(open('data/area.csv', 'r'))
        population_reader = csv.reader(open('data/population.csv', 'r'))

        for i in xrange(186):
            gdp_row = gdp_reader.next()
            key = gdp_row[1]
            gdp = float(gdp_row[2])
            area = float(area_reader.next()[2])
            population = float(population_reader.next()[2])
            self[key] = {'area': area, 'gdp': gdp, 'population': population, 'label': 0}

        self.gdps, self.areas, self.populations = [], [], []
        for key in self:
            self.gdps.append(self[key]['gdp'])
            self.areas.append(self[key]['area'])
            self.populations.append(self[key]['population'])

        self.gdps = numpy.array(self.gdps)
        self.areas = numpy.array(self.areas)
        self.populations = numpy.array(self.populations)

        self.gdps_std = std(self.gdps)
        self.areas_std = std(self.areas)
        self.populations_std = std(self.populations)

        self.gdps = numpy.log(self.gdps / self.gdps_std)
        self.areas = numpy.log(self.areas / self.areas_std)
        self.populations = numpy.log(self.populations / self.populations_std)


    def plot_1D(self, ax='gdps', bins=10):
        ys = sorted(self.__getattribute__(ax))
        fig = plt.figure()
        plt.hist(ys, bins=bins, normed=True)
        plt.ylabel(ax)
        plt.show()

    def plot_2D(self, ax_1='gdps', ax_2='areas'):
        xs, ys = self.__getattribute__(ax_1), self.__getattribute__(ax_2)
        fig = plt.figure()
        plt.scatter(xs, ys)
        plt.xlabel(ax_1)
        plt.ylabel(ax_2)
        plt.show()

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.gdps, self.areas, self.populations)

        ax.set_xlabel('GDP')
        ax.set_ylabel('Area')
        ax.set_zlabel('Population')

        plt.show()

    def max(self, ax='gdps'):
        ys = self.__getattribute__(ax)
        return max(ys)

    def zip(self):
        return zip(self.gdps.T, self.areas.T, self.populations.T)

    def get_data_of(self, country):
        country = self[country]
        return numpy.log(country['gdp'] / self.gdps_std), numpy.log(country['area'] / self.areas_std), numpy.log(country['population'] / self.populations_std)