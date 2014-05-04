from functools import wraps
import operator

from selenium.webdriver import Firefox
from selenium.webdriver import PhantomJS


def new_method_proxy(func):
    def inner(self, *args):
        return func(self._browser, *args)
    return inner


class BrowserTestWrapper(object):
    def __init__(self, browser):
        self._browser = browser

    def __getattr__(self, item):
        return getattr(self._browser, item)

    def __del__(self):
        self._browser.close()

    __str__ = new_method_proxy(str)
    __repr__ = new_method_proxy(str)
    __unicode__ = new_method_proxy(unicode)
    __class__ = property(new_method_proxy(operator.attrgetter('__class__')))
    __eq__ = new_method_proxy(operator.eq)
    __hash__ = new_method_proxy(hash)
    __nonzero__ = new_method_proxy(bool)


class LazyList(object):
    def __init__(self, setup):
        self._setup = setup

    def __iter__(self):
        try:
            value = self._wrapped
        except AttributeError:
            value = self._wrapped = self._setup()

        return iter(value)


BROWSERS = LazyList(
    lambda: [
        BrowserTestWrapper(Firefox()),
        BrowserTestWrapper(PhantomJS()),
    ]
)


def browser_generator(func):
    @wraps(func)
    def _test_all_browsers_inner(self):
        for browser in BROWSERS:
            yield (func, self, browser)

    return _test_all_browsers_inner

