from unittest import TestCase

from should_dsl import should

from selenium_finders.finders import core


class TextFinderTestCase(TestCase):
    def test_should_generate_xpath_for_tag_name(self):
        finder = core.Finder('div')
        finder.to_xpath() | should | equal_to('//div')

    def test_should_generate_xpath_for_attributes(self):
        finder = core.Finder(attributes={'class': 'someclass', 'id': 'someid'})
        finder.to_xpath() | should | equal_to('//*[@class="someclass" and @id="someid"]')

    def test_should_generate_xpath_for_path(self):
        finder = core.Finder(path='test')
        finder.to_xpath() | should | equal_to('test*')

    def test_should_generate_xpath_for_descendent(self):
        finder = core.Finder().descendent('test')
        finder.to_xpath() | should | equal_to('//*/test')
