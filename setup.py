# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

tests_require = [
    'Django>=1.3',
    'nose>1.3',
    'mock==1.0.1',
    'coveralls',
    'factory_boy',
    'webtest',
    'django-webtest',
    'south',
    'xmltodict',
    'django-annoying',
]

setup(
    name='django-pay2pay',
    version='0.9.4',
    packages=['pay2pay'],
    include_package_data=True,
    license='MIT',
    description='A simple Django app for pay via pay2pay.ru system.',
    long_description=README,
    url='http://github.com/drmartiner/django-pay2pay/',
    author='DrMartiner',
    author_email='DrMartiner@GMail.Com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.3',
        'south',
        'xmltodict',
        'django-annoying',
    ],
)