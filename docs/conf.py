# sphinx configuration

project = u'ploneintranet.workspace'

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
]
master_doc = 'index'

# Readme is manually included in index
exclude_patterns = ['README.rst', ]

language = 'en'
