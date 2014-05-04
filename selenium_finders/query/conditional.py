from selenium_finders import XPath


class OrQuery(XPath):
    def __init__(self, *elements):
        self.elements = elements

    def to_xpath(self):
        return '|'.join(element.to_xpath() for element in self.elements)

    def descendent(self, name):
        raise ValueError('Cannot select descendent on a query object')
