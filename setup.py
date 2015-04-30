# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0b1.dev0'
description = 'Helper viewlets to easily insert code on the layout of a Plone site.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='collective.blueline',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='https://github.com/simplesconsultoria/collective.blueline',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'plone.app.layout',
        'plone.app.registry',
        'plone.app.upgrade',
        'plone.directives.form',
        'Products.CMFCore',
        'Products.CMFPlone >=4.3',
        'Products.CMFQuickInstallerTool',
        'Products.GenericSetup',
        'setuptools',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'AccessControl',
            'plone.app.robotframework',
            'plone.app.testing [robot] >=4.2.2',
            'plone.browserlayer',
            'plone.registry',
            'plone.testing',
            'robotsuite',
            'zope.component',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
