from quyckplot import DataSet
from quyckplot.utils import RegexPatterns as RP, format_value_error
from quyckplot.Plotter import Plotter
from quyckplot.Regression import Regression

Plotter.start_session()

data = DataSet.from_regex(
    regex=f"y={RP.FLOAT}x+{RP.FLOAT}.csv",
    name_format="y={slope}x+{intercept}.csv",
    dir="data",
    names=["x", "y"],
    skiprows=1,
)

data = data[0:3]

def f(file_data):
    # takes a FileData instance and fits it
    result = Regression.linear("x", "y", target="fit")(file_data)
    file_data.update_context({"fit_equation": 
        format_value_error(result.slope, result.stderr, toTeX=True) + 
        "x+" + 
        format_value_error(result.intercept, result.intercept_stderr, toTeX=True)
    })
    
data.sequence([
    f,
    lambda d: Plotter.new_plot("x", "y", f"y={d.context['slope']}x+{d.context['intercept']}"), # create a new plot
    Plotter.scatter(x="x", y="y", marker=".", s=1), # scatter the raw data
    Plotter.plot(x="x", y="fit", legend="${fit_equation}$"), # plot the fit
])

Plotter.end_session()