from setuptools import setup, find_packages

setup(
    name='ngscraper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    author='Ellen',
    description='A scraper for extracting painting information from The National Gallery.',
    url='https://github.com/yourusername/ng-scraper',
    python_requires='>=3.7',
)