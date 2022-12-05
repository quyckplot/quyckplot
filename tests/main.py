from quyckplot import DataSet, Plotter

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
data.scatter(
    x="x",
    y="y",
    marker=".",
    s=1
)

Plotter.end_session()