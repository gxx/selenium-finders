from xpath_dsl import Attribute
from xpath_dsl import Builder

from selenium_finders.constants import ANY


class Finder(object):
    def __new__(cls, tag_name='*', attributes=None, path=ANY):
        xpath = getattr(Builder(), path).node(tag_name)
        if attributes:
            xpath = xpath.where(
                *[Attribute(key).equals(value) for key, value in attributes.iteritems()]
            )

        return xpath
