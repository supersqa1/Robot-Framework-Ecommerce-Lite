
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from robot import errors


class BasePage:

    def __init__(self):
        self.bi = BuiltIn()
        try:
            self.sl = BuiltIn().get_library_instance('SeleniumLibrary')
        except Exception as e:
            if "No library 'SeleniumLibrary' found." in str(e):
                self.sl = BuiltIn().import_library('SeleniumLibrary')
            else:
                raise
