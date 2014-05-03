from itertools import chain


PATH_ANYWHERE = '//'
PATH_PARENT = '../'
PATH_DIRECT_DESCENDENT = '/'


class Finder(object):
    def __init__(self, tag_name='*', attributes=None, path=None):
        self.tag_name = tag_name
        self.path = path or PATH_ANYWHERE
        self.attributes = attributes or {}

    def get_extra_attributes(self):
        return []

    def get_xpath_attributes(self):
        normalized_attributes = [
            ('@{key}'.format(key=key), value) for key, value in self.attributes.iteritems()
        ]
        return [
            '{attribute}="{value}"'.format(attribute=key, value=value)
            for key, value in chain(normalized_attributes, self.get_extra_attributes())
        ]

    def to_xpath(self):
        joined_attributes = ' and '.join(self.get_xpath_attributes())

        xpath = '{path}{tag_name}'.format(path=self.path, tag_name=self.tag_name)
        if joined_attributes:
            xpath += '[{xpath_attributes}]'.format(xpath_attributes=joined_attributes)

        return xpath
