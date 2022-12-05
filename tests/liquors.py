from quyckplot import DataSet, Plotter

Plotter.start_session()

liquors = ["abricotine", "jacouille", "kirsh", "meggy"]

data = DataSet.fromFiles(
    [f"{l}.csv" for l in liquors],
    name_format="<liquor>.csv",
    dir="data",
    skiprows=1,
)

data.plot(
    legend="<liquor>"
)

Plotter.end_session()