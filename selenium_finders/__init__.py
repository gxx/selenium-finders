class XPath(object):
    def to_xpath(self):
        raise NotImplementedError()

    def descendent(self, name):
        return DescendentSelector(self, name)


from selenium_finders.selectors.descendent import DescendentSelector
