from selenium_finders import XPath


class DescendentSelector(XPath):
    def __init__(self, expression_object, name):
        self.expression_object = expression_object
        self.name = name

    def to_xpath(self):
        return '{xpath}/{name}'.format(
            xpath=self.expression_object.to_xpath(),
            name=self.name
        )
