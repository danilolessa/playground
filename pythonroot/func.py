import numpy as np
import scipy as sp
import scipy.odr as odr
import matplotlib.pyplot as plt


def odr_fit(func, x, y, sx, sy, beta0=None):
    model = odr.Model(func)
    data = odr.RealData(x, y, sx=sx, sy=sy)
    odr_inst = odr.ODR(data, model, beta0)
    return odr_inst.run()


def plot(x, y, sx=None, sy=None, output=True, fit=None, fit_func=None,
     fit_params=None, residuals=False, xlim=None, ylim=None):
    #initial
    if sx is None:
        sx = np.zeros(len(x))
    if sy is None:
        sy = np.zeros(len(y))

    #limits
    if xlim is None:
        (xmin, xmax) = (np.min(x), np.max(x))
    else:
        (xmin, xmax) - (xlim[0], xlim[1])
    if ylim is None:
        (ymin, ymax) = (np.min(y), np.max(y))
    else:
        (ymin, ymax) - (ylim[0], ylim[1])

    #data ploting
    plt.errorbar(x, y, xerr=sx, yerr=sy, fmt='.')

    #fitting
    if fit is True and fit_params is not None:
        fit_output = odr_fit(fit_func, x, y, sx, sy, fit_params)
        x_fit = np.linspace(xmin, xmax, 1e5)
        y_fit = fit_func(fit_output.beta, x_fit)
        plt.plot(x_fit, y_fit, 'k-')

    if output is True:
        plt.show()

