from unittest import TestCase

from should_dsl import should

from selenium_finders.finders import label


class LabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.LabelFinder('Sign In')
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.LabelFinder('Sign In', tag_name='div')
        finder.to_xpath() | should | equal_to(
            '//div[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.LabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//*[@class="someclass" and '
            '@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.LabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[@class="someclass" and '
            'lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_descendent(self):
        finder = label.LabelFinder('Sign In').descendent('test')
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]/test'
        )
