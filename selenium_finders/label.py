from xpath_dsl import Attribute, Text
from xpath_dsl.builder import Builder

from selenium_finders.constants import ANY
from selenium_finders.constants import PARENT
from selenium_finders.core import Finder
from selenium_finders.text import TextFinder


class UnwrappedLabelFinder(TextFinder):
    def __new__(cls, name, tag_name='*', attributes=None, label_attributes=None, path=ANY):
        if not attributes:
            attributes = {}

        label_xpath = super(UnwrappedLabelFinder, cls).__new__(
            cls,
            name,
            tag_name='label',
            attributes=label_attributes,
            path=PARENT
        ).descendant(Attribute('for'))

        attributes['id'] = label_xpath
        return Finder(tag_name=tag_name, attributes=attributes, path=path)


class UnnestedWrappedLabelFinder(TextFinder):
    def __new__(cls, name, tag_name='*', attributes=None, label_attributes=None, path=ANY):
        label_xpath = super(UnnestedWrappedLabelFinder, cls).__new__(
            cls,
            name,
            tag_name='label',
            attributes=label_attributes,
            path=path
        )
        xpath = label_xpath.descendant(tag_name)
        if attributes:
            xpath = xpath.where(
                *[Attribute(key).equals(value) for key, value in attributes.iteritems()]
            )

        return xpath


class NestedWrappedLabelFinder(object):
    def __new__(cls, name, tag_name='*', attributes=None, label_attributes=None, path=ANY):
        xpath = getattr(Builder(), path).node('label').where(
            Builder().current.any.node.text.normalized.equals(name)
        )
        if label_attributes:
            xpath = xpath.where(
                *[Attribute(key).equals(value) for key, value in label_attributes.iteritems()]
            )

        xpath = xpath.descendant(tag_name)
        if attributes:
            xpath = xpath.where(
                *[Attribute(key).equals(value) for key, value in attributes.iteritems()]
            )

        return xpath


class WrappedLabelFinder(object):
    def __new__(cls, name, tag_name='*', attributes=None, label_attributes=None, path=ANY):
        # //label//*[normalize-space(text())="This is a label"]/ancestor::label//input
        xpath = Finder('label', attributes=label_attributes, path=path)
        xpath = xpath.any.where(
            Text().normalized.equals(name)
        ).ancestor('label').any.node(tag_name)
        return xpath


class LabelFinder(object):
    def __new__(self, name, tag_name='*', attributes=None, label_attributes=None):
        # // label[descendant - or -self::*[normalize - space(text()) = "This is a label"]] // input
        xpath = Builder().any.node('label').where(
            Builder().descendant_or_self.where(
                Text().normalized.equals(name)
            )
        ).any.node('input')
        return xpath
