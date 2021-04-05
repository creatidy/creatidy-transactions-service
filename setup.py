import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="creatidy-transactions-service",
    version="0.0.1",
    author="Adrian Tkacz",
    author_email="",
    description=("Test"),
    license="Property",
    keywords="test",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['protobufs', 'dto'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: Property",
    ],
)
