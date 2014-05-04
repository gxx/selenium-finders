from selenium_finders.finders.core import Finder


class TextFinder(Finder):
    def __init__(self, name, tag_name='*', attributes=None, path=None):
        self.name = name
        super(TextFinder, self).__init__(tag_name=tag_name, attributes=attributes, path=path)

    def get_extra_attributes(self):
        return [('normalize-space(text())', '"{name}"'.format(name=self.name))]
