from unittest import TestCase

from should_dsl import should

from selenium_finders import core


class TextFinderTestCase(TestCase):
    def test_should_generate_xpath_for_tag_name(self):
        finder = core.Finder('div')
        finder.render() | should | equal_to('//div')

    def test_should_generate_xpath_for_attributes(self):
        finder = core.Finder(attributes={'class': 'someclass', 'id': 'someid'})
        finder.render() | should | equal_to('//*[@class="someclass" and @id="someid"]')
