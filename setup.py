"""Setup script for extension."""

from setuptools import setup


setup(
    name='grow-ext-xml-feed',
    version='0.1.0',
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=False,
    packages=[
        'xml_feed',
    ],
    install_requires=[
        'python-dateutil>=2.7.3',
        'protorpc==0.11.1',
        'requests>=2.18.4',
    ],
)
