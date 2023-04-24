import codecs
from setuptools import setup, find_packages

entry_points = {
    "paste.filter_app_factory": [
        "ping = nti.wsgi.ping:ping_handler_factory"
    ],
}


TESTS_REQUIRE = [
    'nti.testing',
    'Paste',
    'WebTest',
    'zope.testrunner',
]


def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()


setup(
    name='nti.wsgi.ping',
    version=_read('version.txt').strip(),
    author='Chris Utz',
    author_email='chris.utz@nextthought.com',
    description="Support for an ops ping endpoing in a WSGI environment",
    long_description=(_read('README.rst') + '\n\n' + _read('CHANGES.rst')),
    url="https://github.com/OpenNTI/nti.wsgi.cors",
    license='Apache',
    keywords='wsgi',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['nti'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools'
    ],
    extras_require={
        'test': TESTS_REQUIRE,
        'docs':  [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'sphinx_rtd_theme',
        ] + TESTS_REQUIRE,
    },
    entry_points=entry_points,
    test_suite="nti.wsgi.ping.tests",
)
