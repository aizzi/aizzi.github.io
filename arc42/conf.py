# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

import os.path
from os import path

import dummy  #TODO enable this line for production version


# -- Project information -----------------------------------------------------

project = "<YOUR_PROJECT_NAME_HERE>"
copyright = "2020, Konica Minolta Inc., All right reserved."
author = "<YOUR_NAME_HERE>"

# The full version, including alpha/beta/rc tags
release = dummy.__version__   #TODO enable this line and remove the next one
#release = "0.0.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.graphviz",
    "sphinx_autodoc_typehints",
    "sphinx.ext.napoleon",
    "sphinx_multiversion",
    "sphinxcontrib.plantuml",
    "sphinx.ext.ifconfig",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "bizstyle"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]

# Other configurations
numfig = True
numfig_format = {"figure": "Fig. %s ", "table": "Table %s ", "code-block": "Ex %s "}
todo_include_todos = True

# -- Option to define a local environment for development purpose ----

# This should help in using a different approach to render plantuml modules
# in a local environment with access to a remote plantuml server.

# Create a file called 'localenv' in your environment, then use the
# ..ifconfig:: directive to specify different content.


def setup(app):
    app.add_config_value("localenv", False, "env")


if os.path.exists("localenv"):
    localenv = True
    plantuml = "java -jar <PATH_TO_YOUR>/plantuml.jar"
    #plantuml = "java -jar C:/Users/CZ100003/AppData/Local/Plantuml/plantuml.jar"
else:
    plantuml = "/usr/bin/plantuml"
plantuml_output_format = "png"
