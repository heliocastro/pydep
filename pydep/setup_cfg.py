from os import path
import sys
if sys.version_info[0] >= 3:
    import configparser
else:
    import ConfigParser as configparser


def setup_cfg_info_dir(rootdir):
    """
    Returns (metadata, error_string) tuple. error_string is None if no error.
    Uses setup_info_cfg to get package metadata for the directory.
    """
    setupfile = path.join(rootdir, 'setup.cfg')
    if not path.exists(setupfile):
        return None, setupfile + ' does not exist'
    return setup_cfg_info(setupfile), None


def setup_cfg_info(setupfile):
    """Returns metadata for a PyPI package by parsing its setup.cfg file."""
    config = configparser.ConfigParser()
    config.read(setupfile)
    metadata = dict(config.items('metadata'))
    options = dict(config.items('options'))
    return {
        'rootdir': None,
        'project_name': metadata['name'] if 'name' in metadata else None,
        'version': metadata['version'] if 'version' in metadata and ':' not in metadata['version'] else None,
        'repo_url': metadata['url'] if 'url' in metadata else None,
        'packages': options['packages'] if 'packages' in options else None,
        'modules': options['py_modules'].strip().split('\n') if 'py_modules' in options else None,
        'scripts': options['scripts'] if 'scripts' in options else None,
        'author': metadata['author'] if 'author' in metadata else None,
        'description': metadata['description'] if 'description' in metadata else None,
        'license': metadata['license'] if 'license' in metadata else None,
        'classifiers': metadata['classifiers'].strip().split('\n') if 'classifiers' in metadata else None,
    }
