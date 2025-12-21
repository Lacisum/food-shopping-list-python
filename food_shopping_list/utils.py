import os
import sys
from typing import Any

import yaml

from food_shopping_list.exceptions import FileFormatError




def read_yaml_file(file_name: str, search_in_the_library: bool = False) -> Any:
    """
    Reads the provided YAML file.

    Args:
        file_name (str): the name of the file to read
        search_in_the_library (bool): if True, searches the file in the library
            instead of the current working directory

    Returns:
        Any: the content of the file.
    """
    if search_in_the_library:
        __location__ = os.path.realpath(
                os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file_path = os.path.join(__location__, file_name)
    else:
        file_path = file_name
    with open(file_path, 'r') as file:
        try:
            content: Any = yaml.safe_load(file)
        except Exception as e:
            print(e, file=sys.stderr)
            sys.exit(1)
    return content




def print_file_format_error(file_name: str, exception: FileFormatError):
    """
    Prints a file format error.

    Args:
        file_name (str): the name of the file
        exception (str): the raised exception
    """
    print(f"Error in {file_name}: {exception}", file=sys.stderr)
