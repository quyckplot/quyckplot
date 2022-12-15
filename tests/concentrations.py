from quyckplot import DataSet, Plotter, RegexPatterns
from quyckplot.utils import sequence

Plotter.start_session() 

# Load data for files in data folder in the format ethanol<concentration>-methanol<concentration>-small.csv for ethanol concentrations from 10 to 90%
data = DataSet.from_regex(
    regex=f"ethanol{RegexPatterns.INT}-methanol{RegexPatterns.INT}-small.csv",
    name_format="ethanol{eth}-methanol{meth}-small.csv",
    dir="data",
    skiprows=1,
    names=["Raman shift", "Intensity"],
)

# Plot data on a single plot
Plotter.new_plot("Raman shift", "Intensity", "Ethanol concentrations")
data.map(
    Plotter.plot(x="Raman shift", y="Intensity", legend="ethanol: {eth}%")
)

# or scatter the data on different plots
data.map(
    sequence([
        lambda d: Plotter.new_plot("Raman shift", "Intensity", f"Ethanol: {d.context['eth']}%"),
        Plotter.scatter(x="Raman shift", y="Intensity", marker=".", s=1),
    ])
)

Plotter.end_session()

"""
In the future, it would be nice to be able to do something like this:

with Plotter.new_plot("Raman shift", "Intensity", "Ethanol concentrations", legend=True) as plot:
    data.map(
        plot.plot(x="Raman shift", y="Intensity", legend="ethanol: {eth}%")
    )

Plotter.end_session()
"""