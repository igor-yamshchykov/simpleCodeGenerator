from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SimpleCodeGenerator',
    version='0.0.1',

    description='This project is generating routine code chunks from templates folder to destination folder',
    long_description=long_description,

    url='https://github.com/igor-yamshchykov/simpleCodeGenerator',

    author='Ihor Yamshchykov',
    author_email='ihor.yamshchykov@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Helper Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 2.7.13',
    ],

    keywords='template, code generator',

    py_modules=["Templater"],
)
