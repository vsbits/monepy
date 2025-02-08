import sys
from pathlib import Path

# -- Project information -----------------------------------------------------

project = "Currency"
copyright = "2025, Vítor Araujo"
author = "Vítor Araujo"
release = "0.1"

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary", "myst_parser"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, str(Path("..", "..", "src").resolve()))
