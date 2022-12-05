from quyckplot import DataSet, Plotter

Plotter.start_session()

# load white sugar data
white_sugar = DataSet.fromFiles(
    ['liquid-white-sugar.csv', 'solid-white-sugar.csv'],
    name_format="<state>-white-sugar.csv",
    dir="data",
    skiprows=1,
)

# load brown sugar data
brown_sugar = DataSet.fromFiles(
    ['liquid-brown-sugar.csv', 'solid-brown-sugar.csv'],
    name_format="<state>-brown-sugar.csv",
    dir="data",
    skiprows=1,
)

# plot white sugar data
white_sugar.plot(legend="<state>")
# plot brown sugar data
brown_sugar.plot(legend="<state>")

Plotter.end_session()