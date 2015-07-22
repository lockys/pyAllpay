# -*- coding: UTF-8 -*-
try:
    from setuptools import setup
except:
    from distutils.core import setup

__version__ = '0.0.12.dev0'
__author__ = 'Calvin Jeng'
__email__ = 'lock4567@gmail.com'

long_description = """
This is allPay(歐付寶) SDK implemented in Python. not All functions are implemented now.
CheckOutString(), CheckOut(), CheckOutFeedback() has been implemented. In general, it could be used in web developed by Django ..etc
Features:
Checkout a payment with following method.
- CVS
- ATM
- WebATM
- BarCode
- Credit card
Dealing with the POST data After the a payment creates or the customer pay the payment.
Check out github repo: https://github.com/lockys/allPay.py
"""


setup(
    name='pyallpay',
    version=__version__,
    author=__author__,
    author_email=__email__,
    packages=['pyallpay', ],
    url='https://github.com/lockys/allpay.py',
    license='LICENSE',
    description='allPay API in python',
    long_description=long_description,
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
