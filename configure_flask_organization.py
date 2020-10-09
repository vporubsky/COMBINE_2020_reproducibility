'''Generate static and templates directories in the current working directory
to allow for proper hierarchical organization for flask to access html and
associated files.'''
from os import path, getcwd, mkdir

# Create directory 'static'
if not path.exists(getcwd() + '/static'):
    mkdir(getcwd() + '/static')
    print('Made directory: static')

# Create directory 'templates'
if not path.exists(getcwd() + '/templates'):
    mkdir(getcwd() + '/templates')
    print('Made directory: templates')

