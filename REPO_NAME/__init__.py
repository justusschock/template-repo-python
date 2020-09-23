__version__ = '0.0.1'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__author__ = 'AUTHOR_NAME'
__author_email__ = 'AUTHOR_EMAIL'
__license__ = 'LICENSE'
__copyright__ = 'Copyright (c) 2020, %s.' % __author__
__homepage__ = 'https://github.com/GITHUB_NAME/REPO_NAME'

# this has to be simple string, see: https://github.com/pypa/twine/issues/522
__docs__ = "PACKAGE_DESCRIPTION"
__long_docs__ = ""
