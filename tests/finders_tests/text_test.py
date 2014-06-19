from unittest import TestCase

from should_dsl import should

from selenium_finders import text


class TextFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = text.TextFinder('Sign In')
        finder.render() | should | equal_to(
            '//*[normalize-space(text())="Sign In"]'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = text.TextFinder('Sign In', tag_name='div')
        finder.render() | should | equal_to('//div[normalize-space(text())="Sign In"]')

    def test_should_generate_xpath_for_attributes(self):
        finder = text.TextFinder('Sign In', attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//*[@class="someclass"][normalize-space(text())="Sign In"]'
        )

    def test_should_generate_xpath_for_descendent(self):
        finder = text.TextFinder('Sign In').descendant('test')
        finder.render() | should | equal_to('//*[normalize-space(text())="Sign In"]/test')
