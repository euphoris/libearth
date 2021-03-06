import os.path
import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import find_packages, setup
from setuptools.command.test import test

from libearth.version import VERSION


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except (IOError, OSError):
        return ''


class pytest(test):

    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from pytest import main
        errno = main(self.test_args)
        raise SystemExit(errno)


install_requires = []
if sys.version_info < (3, 2):
    install_requires.append('futures')


setup(
    name='libearth',
    version=VERSION,
    description='The shared common library for Earth Reader apps',
    long_description=readme(),
    url='http://libearth.earthreader.org/',
    author='Hong Minhee',
    author_email='minhee' '@' 'dahlia.kr',
    license='MIT License',
    packages=find_packages(exclude=['tests']),
    entry_points='''
        [libearth.repositories]
        file = libearth.repository:FileSystemRepository
    ''',
    install_requires=install_requires,
    tests_require=['pytest >= 2.3.0', 'mock >= 1.0.1'],
    cmdclass={'test': pytest},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML'
    ]
)
