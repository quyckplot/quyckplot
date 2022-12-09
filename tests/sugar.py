from quyckplot import DataSet, Plotter

Plotter.start_session()

# load white sugar data
white_sugar = DataSet.from_files(
    ['liquid-white-sugar.csv', 'solid-white-sugar.csv'],
    name_format="{state}-white-sugar.csv",
    dir="data",
    skiprows=1,
    names=["Raman shift", "Intensity"],
)

# load brown sugar data
brown_sugar = DataSet.from_files(
    ['liquid-brown-sugar.csv', 'solid-brown-sugar.csv'],
    name_format="{state}-brown-sugar.csv",
    dir="data",
    skiprows=1,
    names=["Raman shift", "Intensity"],
)

# plot white sugar data
Plotter.new_plot("Raman shift", "Intensity", "White sugar")
white_sugar.map(
    Plotter.scatter(x="Raman shift", y="Intensity", legend="{state}", marker=".", s=1)
)

# do the same for brown sugar
Plotter.new_plot("Raman shift", "Intensity", "Brown sugar")
brown_sugar.map(
    Plotter.scatter(x="Raman shift", y="Intensity", legend="{state}", marker=".", s=1)
)


Plotter.end_session()