from setuptools import setup, find_packages

version = '1.0'

setup(name='ploneintranet.workspace',
      version=version,
      description="A Workspace implementation for ploneintranet",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/ploneintranet/ploneintranet.workflow',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['ploneintranet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.workspace',
          'plone.api',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing[robot]>=4.2.2']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=[],

      )
