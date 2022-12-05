from quyckplot import DataSet, Plotter

Plotter.start_session()

# Load data
data = DataSet()
data.loadFromFileNames(
    ['abricotine.csv'],
    name_format="abricotine.csv",
    dir="data",
    skiprows=1,
    names=["x", "y"],
)

# Plot data
Plotter.plot(
    data,
    x="x",
    y="y",
)

Plotter.end_session()