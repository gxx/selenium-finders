from unittest import TestCase

from should_dsl import should

from selenium_finders import label


class UnwrappedLabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.UnwrappedLabelFinder('Sign In')
        finder.render() | should | equal_to(
            '//*[@id=../label[normalize-space(text())="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.UnwrappedLabelFinder('Sign In', tag_name='div')
        finder.render() | should | equal_to(
            '//div[@id=../label[normalize-space(text())="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.UnwrappedLabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//*[@class="someclass" and @id=../label[normalize-space(text())="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.UnwrappedLabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//*[@id=../label[@class="someclass"][normalize-space(text())="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_descendent(self):
        finder = label.UnwrappedLabelFinder('Sign In').descendant('test')
        finder.render() | should | equal_to(
            '//*[@id=../label[normalize-space(text())="Sign In"]/@for]/test'
        )


class UnnestedWrappedLabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.UnnestedWrappedLabelFinder('Sign In')
        finder.render() | should | equal_to(
            '//label[normalize-space(text())="Sign In"]/*'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.UnnestedWrappedLabelFinder('Sign In', tag_name='div')
        finder.render() | should | equal_to(
            '//label[normalize-space(text())="Sign In"]/div'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.UnnestedWrappedLabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//label[normalize-space(text())="Sign In"]/*[@class="someclass"]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.UnnestedWrappedLabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//label[@class="someclass"][normalize-space(text())="Sign In"]/*'
        )

    def test_should_generate_xpath_for_descendant(self):
        finder = label.UnnestedWrappedLabelFinder('Sign In').descendant('test')
        finder.render() | should | equal_to(
            '//label[normalize-space(text())="Sign In"]/*/test'
        )


class NestedWrappedLabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.NestedWrappedLabelFinder('Sign In')
        finder.render() | should | equal_to(
            '//label[normalize-space(.//*/text())="This is a label"]/*'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.NestedWrappedLabelFinder('Sign In', tag_name='div')
        finder.render() | should | equal_to(
            '//label[normalize-space(.//*/text())="This is a label"]/div'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.NestedWrappedLabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//label[normalize-space(.//*/text())="This is a label"]/*[@class="someclass"]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.NestedWrappedLabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//label[normalize-space(.//*/text())="This is a label"][@class="someclass"]/*'
        )

    def test_should_generate_xpath_for_descendant(self):
        finder = label.NestedWrappedLabelFinder('Sign In').descendant('test')
        finder.render() | should | equal_to(
            '//label[normalize-space(.//*/text())="This is a label"]/*/test'
        )


class LabelFinderTestCase(TestCase):
    def test_should_generate_xpath_for_name_only(self):
        finder = label.LabelFinder('Sign In')
        finder.render() | should | equal_to(
            '//*[@id=../label[normalize-space(text())="Sign In"]/@for]'
            '|//label[normalize-space(text())="Sign In"]/*'
            '|//label[normalize-space(.//*/text())="This is a label"]/*'
        )

    def test_should_generate_xpath_for_tag_name(self):
        finder = label.LabelFinder('Sign In', tag_name='div')
        finder.render() | should | equal_to(
            '//div[@id=../label[normalize-space(text())="Sign In"]/@for]'
            '|//label[normalize-space(text())="Sign In"]/div'
            '|//label[normalize-space(.//*/text())="This is a label"]/div'
        )

    def test_should_generate_xpath_for_attributes(self):
        finder = label.LabelFinder('Sign In', attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//*[@class="someclass" and @id=../label[normalize-space(text())="Sign In"]/@for]'
            '|//label[normalize-space(text())="Sign In"]/*[@class="someclass" '
            'and @id=../label[normalize-space(text())="Sign In"]/@for]'
            '|//label[normalize-space(.//*/text())="This is a label"]'
            '/*[@class="someclass" and @id=../label[normalize-space(text())="Sign In"]/@for]'
        )

    def test_should_generate_xpath_for_label_attributes(self):
        finder = label.LabelFinder('Sign In', label_attributes={'class': 'someclass'})
        finder.render() | should | equal_to(
            '//*[@id=../label[@class="someclass"][normalize-space(text())="Sign In"]/@for]'
            '|//label[@class="someclass"][normalize-space(text())="Sign In"]/*'
            '|//label[normalize-space(.//*/text())="This is a label"][@class="someclass"]/*'
        )
