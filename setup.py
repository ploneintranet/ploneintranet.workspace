from setuptools import setup, find_packages

version = '1.1.dev0'

setup(name='ploneintranet.workspace',
      version=version,
      description="A Workspace implementation for ploneintranet",
      long_description=open("README.rst").read() + "\n" +
                  open("CONTRIBUTORS.txt").read() + "\n" +
                  open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone workspace collaboration intranet',
      author='Plone Intranet Consortium',
      author_email='',
      url='https://github.com/ploneintranet/ploneintranet.workspace',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['ploneintranet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.workspace',
          'plone.api>=1.2.1',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          'Products.CMFPlacefulWorkflow',
          'ploneintranet.invitations',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.app.robotframework',
          ],
          'develop': [
              'Sphinx',
              'zest.releaser',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
