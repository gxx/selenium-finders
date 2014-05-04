import os

from should_dsl import should

from integration_tests.helpers import browser_generator
from selenium_finders.finders import label


TEST_HTML_LOCATION = 'file://{location}'.format(
    location=os.path.abspath(os.path.join(os.path.dirname(__file__), 'label_test.html'))
)


class UnwrappedLabelFinderIntegrationTestCase(object):
    @browser_generator
    def test_should_find_element_by_name_only(self, browser):
        xpath = label.UnwrappedLabelFinder('This is a label').to_xpath()

        browser.get(TEST_HTML_LOCATION)
        elements = browser.find_elements_by_xpath(xpath)

        elements | should | have(1).element
        elements[0].get_attribute('value') | should | equal_to('Unwrapped Label')
