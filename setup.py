#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.validator',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.validator'],
    version='0.01',
    description='Simple Python wrapper for Who\'s On First helper functions',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-validator',
    install_requires=[
        'mapzen.whosonfirst.utils',
        'mapzen.whosonfirst.export',
        'mapzen.whosonfirst.placetypes',
        'geojson',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-dump-concordances-local',
        'scripts/wof-dump-hierarchies',
        'scripts/wof-dump-superseded',
        'scripts/wof-concordances-to-db',
        'scripts/wof-id2git',
        'scripts/wof-inventory-properties',
        'scripts/wof-placetype-to-csv',
        'scripts/wof-promote-geometry',
        'scripts/wof-properties',
        'scripts/wof-csv-to-feature-collection',
        'scripts/wof-csv-to-s3',
        'scripts/wof-mk-place',
        'scripts/wof-supersede',
        'scripts/wof-validate',
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-validator/releases/tag/v0.01',
    license='BSD')
