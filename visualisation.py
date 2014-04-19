from scipy.stats import pearsonr
from data.data_container import DataContainer3DCsv

__author__ = 'Ramin'

dc = DataContainer3DCsv()
# print dc.max(), dc.max('areas'), dc.max('populations')
# dc.plot()
# dc.plot_1D(ax='areas')
dc.plot_2D(ax_1='gdps', ax_2='populations')

print pearsonr(dc.areas, dc.populations)