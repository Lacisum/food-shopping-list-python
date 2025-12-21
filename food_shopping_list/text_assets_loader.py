from typing import Any

from food_shopping_list.exceptions import FileFormatError
from food_shopping_list.utils import read_yaml_file, print_file_format_error




class TextAssetsLoader:
    """Class to load text assets."""




    def __init__(self, file_name: str):
        self.file_name: str = file_name




    def load(self) -> dict:
        """Loads the content of the file and checks its correctness.

        Returns:
            dict: the content of the file

        Raises:
            FileFormatError: if the content of the file is incorrect
        """
        content = read_yaml_file(self.file_name, search_in_the_library=True)
        try:
            self._check_content_correctness(content)
        except FileFormatError as e:
            print_file_format_error(self.file_name, e)
        return content




    def _check_content_correctness(self, content: Any) -> None:
        """Raises an exception is the content is incorrect.

        The correctness check is loose: keys are not checked.

        Raises:
            FileFormatError: if the content is incorrect
        """
        if not isinstance(content, dict):
            raise FileFormatError('the root element is not a dictionary')
        for text_key, text in content.items():
            if not isinstance(text, str):
                raise FileFormatError(f"the value of the key '{text_key}' is not a a string")
