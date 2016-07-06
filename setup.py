from distutils.core import setup
from setuptools import find_packages
import codecs

def long_description():
    with codecs.open('README.rst', 'r') as f:
        return f.read()

setup(
    name = 'fakegit',
    packages = find_packages(),
    version = '0.1',
    description = 'A great tool to fool yourself and others',
    long_description = long_description(),
    author = 'SuperFashi',
    author_email = 'admin@superfashi.com',
    url = 'https://github.com/hanbang-wang/FakeGit',
    download_url = 'https://github.com/hanbang-wang/FakeGit/tarball/master',
    keywords = ['git', 'fakegit'],
    classifiers = ['Development Status :: 5 - Production/Stable', 'License :: Freely Distributable'],
    entry_points = {'console_scripts': ['fakegit = fakegit.main:main']},
    install_requires = ['requests'],
    license = 'Unlicense',
)
