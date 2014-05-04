from selenium_finders.finders.core import Finder
from selenium_finders.finders.core import PATH_DIRECT_DESCENDENT
from selenium_finders.finders.core import PATH_PARENT
from selenium_finders.finders.text import TextFinder
from selenium_finders.query.conditional import OrQuery


class LabelFinderBase(TextFinder):
    def __init__(self, name, tag_name='*', attributes=None, label_attributes=None, path=None):
        self.label_attributes = label_attributes
        super(LabelFinderBase, self).__init__(
            name,
            tag_name=tag_name,
            attributes=attributes,
            path=path
        )


class UnwrappedLabelFinder(LabelFinderBase):
    def get_extra_attributes(self):
        label_finder = TextFinder(
            self.name,
            tag_name='label',
            attributes=self.label_attributes,
            path=PATH_PARENT
        )
        return [('@id', label_finder.descendent('@for').to_xpath())]


class WrappedLabelFinder(LabelFinderBase):
    def to_xpath(self):
        label_finder = TextFinder(
            self.name,
            tag_name='label',
            attributes=self.label_attributes,
        )
        element_finder = Finder(
            tag_name=self.tag_name,
            attributes=self.attributes,
            path=PATH_DIRECT_DESCENDENT
        )
        return '{label}{element}'.format(
            label=label_finder.to_xpath(),
            element=element_finder.to_xpath()
        )


class LabelFinder(object):
    def __new__(self, name, tag_name='*', attributes=None, label_attributes=None, path=None):
        query = OrQuery(
            UnwrappedLabelFinder(
                name,
                tag_name=tag_name,
                attributes=attributes,
                label_attributes=label_attributes,
                path=path
            ),
            WrappedLabelFinder(
                name,
                tag_name=tag_name,
                attributes=attributes,
                label_attributes=label_attributes,
                path=path
            ),
        )
        return query
