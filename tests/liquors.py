from quyckplot import DataSet, Plotter
from quyckplot.utils import sequence

def some_function(file_data):
    # this is a dummy function to test the sequence and map combo.
    # it adds a column named "z" to the data. z = 2 * y
    file_data.data["z"] = 2 * file_data.data["y"]

Plotter.start_session()

liquors = ["abricotine", "jacouille", "kirsh", "meggy"]

data = DataSet.from_files(
    [f"{l}.csv" for l in liquors],
    name_format="{liquor}.csv",
    dir="data",
    skiprows=1,
    names=["x", "y"]
)

Plotter.new_plot("x", "y", "Liquors")
data.map(
    sequence([
        some_function,
        Plotter.scatter(x="x", y="y", legend="{liquor}", marker=".", s=1),
        Plotter.scatter(x="x", y="z", legend="2{liquor}", marker=".", s=1)
    ])
)

Plotter.end_session()