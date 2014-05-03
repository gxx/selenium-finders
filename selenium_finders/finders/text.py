from selenium_finders.finders.base import BaseFinder


class TextFinder(BaseFinder):
    def __init__(self, name, tag_name='*', attributes=None):
        if not attributes:
            attributes = {}

        self.name = name
        self.tag_name = tag_name
        self.attributes = attributes

    def get_xpath_attributes(self):
        xpath_attributes = []
        xpath_attributes.append(
            'lower-case(normalize-space(text()))="{name}"'.format(name=self.name)
        )
        xpath_attributes.extend(
            '@{attribute}="{value}"'.format(attribute=key, value=value)
            for key, value in self.attributes.iteritems()
        )
        return ' and '.join(xpath_attributes)

    def to_xpath(self):
        return '//{tag_name}[{xpath_attributes}]'.format(
            tag_name=self.tag_name,
            xpath_attributes=self.get_xpath_attributes()
        )
