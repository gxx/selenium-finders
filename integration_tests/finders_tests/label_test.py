import os

from should_dsl import should

from integration_tests.helpers import browser_generator
from selenium_finders import label


TEST_HTML_LOCATION = 'file://{location}'.format(
    location=os.path.abspath(os.path.join(os.path.dirname(__file__), 'label_test.html'))
)


class UnwrappedLabelFinderIntegrationTestCase(object):
    @browser_generator
    def test_should_find_element_by_name_only(self, browser):
        xpath = label.UnwrappedLabelFinder('This is a label').render()

        browser.get(TEST_HTML_LOCATION)
        elements = browser.find_elements_by_xpath(xpath)

        elements | should | have(1).element
        elements[0].get_attribute('value') | should | equal_to('Unwrapped Label')


class UnnestedWrappedLabelFinderIntegrationTestCase(object):
    @browser_generator
    def test_should_find_element_by_name_only(self, browser):
        xpath = label.UnnestedWrappedLabelFinder('This is a label').render()

        browser.get(TEST_HTML_LOCATION)
        elements = browser.find_elements_by_xpath(xpath)

        elements | should | have(1).element
        elements[0].get_attribute('value') | should | equal_to('Unnested Wrapped Label')


class NestedWrappedLabelFinderIntegrationTestCase(object):
    @browser_generator
    def test_should_find_element_by_name_only(self, browser):
        xpath = label.NestedWrappedLabelFinder('This is a label', tag_name='input').render()

        browser.get(TEST_HTML_LOCATION)
        elements = browser.find_elements_by_xpath(xpath)

        elements | should | have(2).element
        elements[0].get_attribute('value') | should | equal_to('Nested Wrapped Label #1')
        elements[0].get_attribute('value') | should | equal_to('Nested Wrapped Label #2')
