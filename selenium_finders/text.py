from xpath_dsl import Text

from selenium_finders.constants import ANY
from selenium_finders.core import Finder


class TextFinder(Finder):
    def __new__(cls, name, tag_name='*', attributes=None, path=ANY):
        xpath = super(TextFinder, cls).__new__(
            cls,
            tag_name=tag_name,
            attributes=attributes,
            path=path
        )
        xpath = xpath.where(Text().normalized.equals(name))
        return xpath
