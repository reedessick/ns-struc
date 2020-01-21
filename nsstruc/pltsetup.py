"""a module that sets up some specific things for matplotlib that we find generally useful"""
__author__ = "philippe.landry@ligo.org"

#-------------------------------------------------

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

#------------------------

plt.rcParams['axes.color_cycle'] = ['black', 'limegreen', 'darkgrey', 'orange', 'cyan', 'hotpink', 'blue', 'darkred']
plt.rcParams['axes.labelsize'] = 28
plt.rcParams['figure.figsize'] = 10, 10
AUTO_COLORS =  plt.rcParams['axes.color_cycle']
AUTO_MARKERS = ['.', '+', 'x', 'd', '1']
AUTO_LINESTYLES = ['-', '--', ':', '-.']

PROPSLABELS = {
    'rhoc': r'$\Delta\rho_c$',
    'M': r'$\Delta M$',
    'R': r'$\Delta R$',
    'Lambda': r'$\Delta\Lambda$',
    'I': r'$\Delta I$',
} 
