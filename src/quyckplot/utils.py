import os
import re
from matplotlib import pyplot as plt

class RegexPatterns:
    INT = '\d+'
    OPT_INT = '\d*'
    FLOAT = f'{INT}\.?\d*'
    OPT_FLOAT = f'{OPT_INT}\.?\d*'

def getFileNamesFromRegex(regex="*", dir=""):
        pattern = re.compile(regex)
        files = os.listdir(dir)
        return [f'{file}' for file in files if pattern.match(file)]

def formatted_string2dict(s, format):
    """
    Converts a string of parameters into a dictionary.
    example:
        - if s = "T=10K-I=1.5A.csv" and format = "T=<temp>K-I=<current>A.csv", the function returns {"temp": "10", "current": "1.5"}
    """
    # get the names of the parameters
    names = re.findall("<.*?>", format) # ["<temp>", "<current>"]
    # remove the "<" and ">" characters
    names = [name[1:-1] for name in names] # ["temp", "current"]
    # remove the parameters from the format
    format = re.sub("<.*?>", "(.*?)", format) # "T=(.*?)K-I=(.*?)A.csv"
    # compile the format
    pattern = re.compile(format) 
    # match the string with the format
    match = pattern.match(s)
    # get the values of the parameters
    values = match.groups() # ("10", "1.5")
    # create the dictionary
    return {name: value for name, value in zip(names, values)}

def dict2formatted_string(dict, format):
    """
    Converts a dictionary of parameters into a string.
    example:
        - if dict = {"temp": "10", "current": "1.5"} and format = "T=<temp>K-I=<current>A.csv", the function returns "T=10K-I=1.5A.csv"
    """
    # get the names of the parameters
    names = re.findall("<.*?>", format) # ["<temp>", "<current>"]
    # remove the "<" and ">" characters
    names = [name[1:-1] for name in names] # ["temp", "current"]
    # replace the parameters in the format
    for name in names:
        format = format.replace(f"<{name}>", dict[name])
    return format

# this function takes a plt method (e.g. plt.plot) and returns a function that takes a dataframe and plots it with the given method
def plotter_factory(method):
    def plotter(cls, data, x, y, xlabel=None, ylabel=None, legend=None, new=True, size=(9, 7), **kwargs):
        """
        Plots the data of the DataSet object.
        """
        if xlabel is None:
            xlabel = x
        if ylabel is None:
            ylabel = y
        if new:
            cls.new_plot(xlabel, ylabel, title="", size=size)
        data.map(lambda df: method(
            df["data"][x],
            df["data"][y],
            label=dict2formatted_string(df["params"], legend) if legend else None,
            **kwargs
        ))
        if legend:
            plt.legend(loc="best")
    return plotter