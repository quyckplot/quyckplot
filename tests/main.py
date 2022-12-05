from quyckplot import DataSet, Plotter

Plotter.start_session() # should be removed in later versions

# Load data
data = DataSet.fromFiles(
    ['abricotine.csv'],
    name_format="abricotine.csv", # should be optional in later versions
    dir="data",
    skiprows=1,
    names=["x", "y"],
)

# Plot data
data.plot(
    xlabel=r"$\rho$",
    ylabel="some other label",
)

Plotter.end_session() # should be removed in later versions


"""
# ideally, later versions should work like this:
# no start_session() or end_session() needed
# name_format optional when loading from files
# columns named "x" and "y" by default
# columns "x" and "y" are the columns that are plotted by default

from quyckplot import DataSet

data = DataSet.fromFiles(
    ['abricotine.csv'],
    dir="data",
    skiprows=1,
)

data.plot()
"""

