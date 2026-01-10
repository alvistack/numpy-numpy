
"""
Module to expose more detailed version info for the installed `numpy`
"""
version = "2.4.0"
__version__ = version
full_version = version

git_revision = "485f1c40703f1c43be708be4c7b7a21b10d90337"
release = 'dev' not in version and '+' not in version
short_version = version.split("+")[0]
