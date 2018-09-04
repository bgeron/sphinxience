__version__ = '0.1.2'

__all__ = []

import os.path

def setup(app):
    app.require_sphinx('1.7')

    app.add_html_theme('sphinxience',
        os.path.abspath(os.path.dirname(__file__)))

    return {'version': '0.1.2'}