import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

__author__ = 'ramin'


class DataContainer(dict):
    def plot(self):
        pass


class DataContainer3DCsv(DataContainer):
    def __init__(self):
        gdp_reader = csv.reader(open('data/gdp.csv', 'r'))
        area_reader = csv.reader(open('data/area.csv', 'r'))
        population_reader = csv.reader(open('data/population.csv', 'r'))

        gdp_max, area_max, population_max = 0, 0, 0

        for i in xrange(186):
            gdp_row = gdp_reader.next()
            key = gdp_row[1]
            gdp = float(gdp_row[2])
            area = float(area_reader.next()[2])
            population = float(population_reader.next()[2])
            if gdp > gdp_max:
                gdp_max = gdp
            if area > area_max:
                area_max = area
            if population > population_max:
                population_max = population
            self[key] = {'area': area, 'gdp': gdp, 'population': population}

        self.gdps, self.areas, self.populations = [], [], []
        for key in self:
            self.gdps.append(self[key]['gdp'])# / gdp_max)
            self.areas.append(self[key]['area'])# / area_max)
            self.populations.append(self[key]['population'])# / population_max)

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

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)


        plt.show()

    def max(self, ax='gdps'):
        ys = self.__getattribute__(ax)
        return max(ys)