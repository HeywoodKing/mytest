# -*- encoding: utf-8 -*-
"""
@File           : setup.py.py
@Time           : 2019/12/30 21:46
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : mytest
@description    : 描述
"""
from distutils.core import setup
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='MyTranslate',
    version='0.1.0',
    description='An efficient and practical translation tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='hywell',
    author_email='opencoding@hotmail.com',
    url='https://www.python.org',
    license='MIT',
    keywords='translate',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',

    },
    py_modules=['pytranslate'],
    # packages=['pytranslate'],
    packages=find_packages(),
    platforms='any',
    install_requires=['requests>=2.22.0', 'fake_useragent>=0.1.11'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'mytranslate=mytranslate:main'
        ],
    },
    classifiers={
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    },
)
