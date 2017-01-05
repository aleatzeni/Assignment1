import sys
import os

extensions = [
    'sphinx.ext.autodoc',  # Support automatic documentation
    'sphinx.ext.coverage', # Automatically check if functions are documented
    'sphinx.ext.mathjax',  # Allow support for algebra
    'sphinx.ext.viewcode', # Include the source code in documentation
    'numpydoc'             # Support NumPy style docstrings
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Greengraph'
copyright = '2016, Alessia Atzeni'
version = '0.1.0'
release = '0.1.0'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'Greengraphdoc'
latex_elements = {
}

latex_documents = [
  ('index', 'Greengraph.tex', 'Greengraph Documentation',
   'Alessia Atzeni', 'manual'),
]

man_pages = [
    ('index', 'greengraph','Greengraph Documentation',
     ['Alessia Atzeni'], 1)
]

texinfo_documents = [
  ('index', 'Greengraph', 'Greengraph Documentation',
   'Alessia Atzeni', 'Greengraph', 'Generate a graph showing the proportion of green pixels between two endpoints.',
   'Miscellaneous'),
]