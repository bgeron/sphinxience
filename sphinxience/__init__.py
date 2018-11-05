__version_tuple__ = (0, 4, 2)
__version__ = '.'.join(map(str, __version_tuple__))
__version_date_latex__ = "2018/10/01" # in LaTeX format

__all__ = []

import logging, os.path
from os import path
from sphinx.locale import __
from sphinx.util.fileutil import copy_asset_file

SUBMODULES = [
    "collapse",
    "skip",
]

TEMPLATE_HTML_ASSET_FILES = [
    "jquery.details.min.js",
]

TEMPLATE_LATEX_ASSET_FILES = [
    "sphinxience-article.cls_t",
    "sphinxience.sty_t",
]

package_dir = path.abspath(path.dirname(__file__))

def html_is_active(app):
    return app.builder.format == 'html'

def latex_is_active(app):
    return app.builder.format == 'latex'

def update_context(app, pagename, templatename, context, doctree):
    context["sphinxience_version"] = __version__

def on_build_finished(app, exc):
    # Copy static files for LaTeX after the rest of the build process is done.

    if exc is None:
        if html_is_active(app):
            context = dict()
            _copy_asset_files(app, TEMPLATE_HTML_ASSET_FILES, ['static'],
                ['_static'], context)

        if latex_is_active(app):
            context = dict(
                sphinxience_version = __version__,
                sphinxience_version_date_latex = __version_date_latex__
            )

            _copy_asset_files(app, TEMPLATE_LATEX_ASSET_FILES, ['templates'],
                [], context)



def _copy_asset_files(app, asset_files,
        src_path_segments, dest_path_segments, context):
    """
    Parameter src_path_segments is a list of path segments to be appended to
    the Sphinxience root directory. Each filename in asset_files must be
    reachable through that path, and will be copied into the given path into
    the current build target directory. Files are copied with copy_asset_file,
    which templates using the given context if the asset filename ends in _t .
    """

    src_path = path.join(package_dir, *src_path_segments)
    dest_path = path.join(app.outdir, *dest_path_segments)
    logger = logging.getLogger(__name__)
    for asset_file in asset_files:
        src_filename = path.join(src_path, asset_file)
        logger.debug(__("Copying file %s into %s" % (src_filename, dest_path)))
        copy_asset_file(src_filename, dest_path, context=context)


def setup(app):
    app.require_sphinx('1.7')

    app.add_html_theme('sphinxience',
        os.path.abspath(os.path.dirname(__file__)))

    app.connect("html-page-context", update_context)
    app.connect("build-finished", on_build_finished)

    for submodule in SUBMODULES:
        app.setup_extension("sphinxience.{}".format(submodule))

    return {'version': __version__, "parallel_read_safe": True}