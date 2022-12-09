from typing import List

from .FileData import FileData
from .utils import file_names_from_regex

class DataSet:
    def __init__(self, data: List[FileData] = None):
        self.data = data if data is not None else []

    def clear(self):
        self.data = []

    @classmethod
    def from_files(cls, file_names, name_format="", dir="", **args):
        """
        Creates a DataSet instance from a list of files.
        """
        return cls([FileData.from_file(name, name_format, dir, **args) for name in file_names])

    @classmethod
    def from_regex(cls, regex="*", dir="", name_format="", **args):
        """
        Creates a DataSet instance from a list of files that match the given regex.
        """
        return cls.from_files(file_names_from_regex(regex, dir), name_format, dir, **args)