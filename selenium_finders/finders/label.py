from selenium_finders.finders.core import PATH_PARENT
from selenium_finders.finders.text import TextFinder


class LabelFinder(TextFinder):
    def __init__(self, name, tag_name='*', attributes=None, label_attributes=None, path=None):
        self.label_attributes = label_attributes
        super(LabelFinder, self).__init__(
            name,
            tag_name=tag_name,
            attributes=attributes,
            path=path
        )

    def get_extra_attributes(self):
        label_finder = TextFinder(
            self.name,
            tag_name='label',
            attributes=self.label_attributes,
            path=PATH_PARENT
        )
        return [('@id', label_finder.descendent('@for').to_xpath())]
