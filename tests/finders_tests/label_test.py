from unittest import TestCase

from should_dsl import should

from selenium_finders.finders import label


class UnwrappedLabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.UnwrappedLabelFinder('Sign In')
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.UnwrappedLabelFinder('Sign In', tag_name='div')
        finder.to_xpath() | should | equal_to(
            '//div[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.UnwrappedLabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//*[@class="someclass" and '
            '@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.UnwrappedLabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[@class="someclass" and '
            'lower-case(normalize-space(text()))="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_descendent(self):
        finder = label.UnwrappedLabelFinder('Sign In').descendent('test')
        finder.to_xpath() | should | equal_to(
            '//*[@id=../label[lower-case(normalize-space(text()))="Sign In"]/@for]/test'
        )


class WrappedLabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.WrappedLabelFinder('Sign In')
        finder.to_xpath() | should | equal_to(
            '//label[lower-case(normalize-space(text()))="Sign In"]/*'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.WrappedLabelFinder('Sign In', tag_name='div')
        finder.to_xpath() | should | equal_to(
            '//label[lower-case(normalize-space(text()))="Sign In"]/div'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.WrappedLabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//label[lower-case(normalize-space(text()))="Sign In"]/*[@class="someclass"]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.WrappedLabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.to_xpath() | should | equal_to(
            '//label[@class="someclass" and lower-case(normalize-space(text()))="Sign In"]/*'
        )

    def test_should_generate_xpath_for_descendent(self):
        finder = label.WrappedLabelFinder('Sign In').descendent('test')
        finder.to_xpath() | should | equal_to(
            '//label[lower-case(normalize-space(text()))="Sign In"]/*/test'
        )
