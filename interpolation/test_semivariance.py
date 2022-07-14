import sys
sys.path.append('basics')
from point import *
import numpy as np
from semivariance import *
from read_data import *
Z = read_data('data-master/necoldem.dat')
hh = 50
lags = np.arange(0, 3000, hh)
gamma = semivar(Z, lags, hh)