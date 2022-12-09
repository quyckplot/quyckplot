"""
A FileData class contains the data from a file and some associated context.
"""

import pandas as pd
import parse

class FileData:
    @classmethod
    def from_file(cls, name, dir="", name_format="", **args):
        """
        Creates a FileData instance from a file.
        """
        path = f"{dir}/{name}"
        # get the data from the file
        data = pd.read_csv(path, **args)
        # get the context from the file name
        parse_result = parse.parse(name_format, name)
        context = {"file_path": path, **parse_result.named}
        return cls(data, context)