import os
import re
from matplotlib import pyplot as plt

class RegexPatterns:
    INT = '\d+'
    OPT_INT = '\d*'
    FLOAT = f'{INT}\.?\d*'
    OPT_FLOAT = f'{OPT_INT}\.?\d*'

def file_names_from_regex(regex=".*", dir=""):
        """
        Returns a list of file names in the given directory that match the given regex.
        """
        pattern = re.compile(regex)
        files = os.listdir(dir)
        return [f'{file}' for file in files if pattern.match(file)]

def sequence(fs):
    """
    Returns a function that applies the given functions in sequence.
    The functions are applied in the order they are given and directly act on the input.
    """
    def function(x):
        for f in fs:
            f(x)
    return function