try:
    from setuptools import setup
except:
    from distutils.core import setup

__version__ = '0.0.7-dev'
__author__ = 'Calvin Jeng'
__email__ = 'lock4567@gmail.com'

setup(
    name='pyallpay',
    version=__version__,
    author=__author__,
    author_email=__email__,
    packages=['pyallpay', ],
    url='https://github.com/lockys/allpay.py',
    license='LICENSE',
    description='allPay API in python',
    long_description=open('README.rst').read(),
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    zip_safe=False,
)
