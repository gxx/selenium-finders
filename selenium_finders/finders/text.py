from selenium_finders.finders.core import Finder


class TextFinder(Finder):
    def __init__(self, name, tag_name='*', attributes=None, path=None):
        self.name = name
        super(TextFinder, self).__init__(tag_name=tag_name, attributes=attributes, path=None)

    def get_extra_attributes(self):
        return [('lower-case(normalize-space(text()))', self.name)]
