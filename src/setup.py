__author__ = "talba"
__date__ = "$10/04/2015 19:47:47$"

from setuptools import setup, find_packages

setup (
       name='HelloPython',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['Operation>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='talba',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )