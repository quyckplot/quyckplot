import os
import re
from matplotlib import pyplot as plt

class RegexPatterns:
    INT = '\d+'
    OPT_INT = '\d*'
    FLOAT = f'{INT}\.?\d*'
    OPT_FLOAT = f'{OPT_INT}\.?\d*'

def getFileNamesFromRegex(regex="*", dir=""):
        """
        Returns a list of file names in the given directory that match the given regex.
        """
        pattern = re.compile(regex)
        files = os.listdir(dir)
        return [f'{file}' for file in files if pattern.match(file)]