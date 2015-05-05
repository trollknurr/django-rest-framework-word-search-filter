#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='djangorestframework-word-filter',
    version='0.1.0',
    url='https://github.com/trollknurr/django-rest-framework-word-search-filter',
    license='MIT',
    description='By word filter backend for Django REST Framework. No db backend special features (work on all db).',
    author='Anton Shtarev',
    author_email='trollknurr@gmail.com',
    packages=get_packages('rest_framework_word_filter'),
    package_data=get_package_data('rest_framework_word_filter'),
    zip_safe=False,
    install_requires=[
        'djangorestframework',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)