from quyckplot import DataSet, Plotter, RegexPatterns

Plotter.start_session() 

# Load data for files in data folder in the format ethanol<concentration>-methanol<concentration>-small.csv for ethanol concentrations from 10 to 90%
data = DataSet.fromRegex(
    regex=f"ethanol{RegexPatterns.INT}-methanol{RegexPatterns.INT}-small.csv",
    name_format="ethanol<eth>-methanol<meth>-small.csv",
    dir="data",
    skiprows=1,
    columns=["Raman shift", "Intensity"],
)

# Plot data
data.plot(
    x="Raman shift",
    y="Intensity",
    legend="<eth>%"
)

Plotter.end_session()