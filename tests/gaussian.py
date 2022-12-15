from quyckplot import DataSet
from quyckplot.utils import RegexPatterns as RP
from quyckplot.Plotter import Plotter
from quyckplot.Regression import Regression
import numpy as np

Plotter.start_session()

data = DataSet.from_regex(
    regex=f"gaussian_a={RP.FLOAT}_c={RP.FLOAT}.csv",
    name_format="gaussian_a={a}_c={c}.csv",
    dir="data",
    names=["x", "y"],
)

def gaussian(x, amplitude, center, width):
    return amplitude * np.exp(-(x - center)**2 / (2 * width**2))

def fit_and_update_context(file_data):
    result = Regression.generic(gaussian, "x", "y", target="fit")(file_data)
    file_data.update_context({"fit_amplitude": result[0][0], "fit_center": result[0][1], "fit_width": result[0][2]})

data = data[0:3]

data.sequence([
    fit_and_update_context,
    lambda d: Plotter.new_plot("x", "y", f"a={d.context['a']}, c={d.context['c']}"), # create a new plot
    Plotter.scatter(x="x", y="y", marker=".", s=1), # scatter the raw data
    Plotter.plot(x="x", y="fit", legend="$c={fit_width}$"), # plot the fit
])

Plotter.end_session()