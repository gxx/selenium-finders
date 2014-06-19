from setuptools import setup

setup(
    name='selenium-finders',
    version='0.0.1',
    author='Andrew Crosio',
    author_email='Andrew.Crosio@gmail.com',
    url='https://github.com/Andrew-Crosio/selenium-finders',
    license='license info',
    description='make a description',
    long_description='make a long description',
    packages=['selenium_finders'],
    include_package_data=True,
    platforms=['any'],
    classifiers=[
        'Topic :: Internet',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Programming Language :: Python :: 2.7',
    ],
    # TODO: determine if this should be in a requirements.txt
    install_requires=[
        'selenium==2.41.0',
        'git+https://github.com/Andrew-Crosio/xpath-dsl.git@master#egg=xpath-dsl',
    ],
    test_suite='tests',
    tests_require=[],
)
