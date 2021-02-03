from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rccnlp',
    packages=['rccnlp'],
    install_requires=['janome'],
    package_data={'rccnlp': ['dic/*.json']},

    version='0.1.0',
    license='MIT',

    author='averak',
    author_email='abe12@mccc.jp',

    url='https://github.com/averak/rccnlp',

    desription='A simple sentiment analysis utility for Japanese.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setiment nlp japanese',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
