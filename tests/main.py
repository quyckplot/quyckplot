from quyckplot import DataSet, Plotter
import matplotlib as mpl
from matplotlib import pyplot as plt

Plotter.start_session()

# Load data
data = DataSet.fromFiles(
    ['abricotine.csv'],
    name_format="abricotine.csv",
    dir="data",
    skiprows=1,
    names=["x", "y"],
)

# Plot data
data.plot(
    x="x",
    y="y",
    xlabel=r"$\rho$",
    ylabel="some other label",
)

Plotter.end_session()