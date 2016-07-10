import numpy as np
import scipy as sp
import scipy.odr as odr
import matplotlib.pyplot as plt

class InstanceOptions:
    name = ""
    title = ""
    def __init__(self):
        return None
    
class AxisOptions:
    axis_title = ""
    axis_interval = None
    axis_log = False
    axis_grad = False
    
    axis_title_style = None
    axis_mark_style = None

class PlotOptions:

    title = None
    windowSize = None
    fontType = None
    backgroundColor = None
    frontgroundColor = None
    pointStyle = None
    errorbarStyle = None
    x_axis_options = None ###
    y_axis_options = None ###
    
    def __init__(self):
        return None

class FitOptions:

    function = None
    parameters = None
    fit = False
    functionStyle = None
    
    #Fitting params
    fit_interval = None    
    fix_parameters = None
    fit_mode = None
    residualPlot_type = None
    residual_axis_options = None ###

    def __init__(self):
        return None

def odr_fit(func, x, y, sx, sy, beta0=None):
    model = odr.Model(func)
    data = odr.RealData(x, y, sx=sx, sy=sy)
    odr_inst = odr.ODR(data, model, beta0)
    return odr_inst.run()




def plot(x, y, sx=None, sy=None, output=True, fitOptions=None, plotOptions=None):
    #initial
    if sx is None:
        sx = np.zeros(len(x))
    if sy is None:
        sy = np.zeros(len(y))

    #data ploting
    ax = plt.figure()
    ax.errorbar(x, y, xerr=sx, yerr=sy, fmt='.')

    #fitting

    if output is True:
        plt.show()
            
    
    return None
    


