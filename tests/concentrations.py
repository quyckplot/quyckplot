from quyckplot import DataSet, Plotter, RegexPatterns

Plotter.start_session() 

# Load data for files in data folder in the format ethanol<concentration>-methanol<concentration>-small.csv for ethanol concentrations from 10 to 90%
data = DataSet.from_regex(
    regex=f"ethanol{RegexPatterns.INT}-methanol{RegexPatterns.INT}-small.csv",
    name_format="ethanol{eth}-methanol{meth}-small.csv",
    dir="data",
    skiprows=1,
    names=["Raman shift", "Intensity"],
)

# Plot data
Plotter.new_plot("Raman shift", "Intensity", "Ethanol concentrations")
data.map(
    Plotter.scatter(x="Raman shift", y="Intensity", legend="ethanol: {eth}%", marker=".", s=1)
)

Plotter.end_session()