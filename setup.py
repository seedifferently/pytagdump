import os, sys
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

extras_require = {
    'YAML': ['PyYAML >= 3.10'],
    'JSON': []
}

if sys.version_info[0] >= 3 or sys.version_info[:2] < (2, 5):
    raise RuntimeError('Requires Python 2.5 or above and does not support '
                       'Python 3')
elif sys.version_info[:2] < (2, 6):
    extras_require['JSON'] = ['simplejson >= 2.3']

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = CHANGES = ''

setup(
    name='pytagdump',
    version='0.3.1',
    author='Seth Davis',
    author_email='seth@curiasolutions.com',
    description="A simple utility to print the ID3/tag info of various " + \
                "files supported by the mutagen package.",
    long_description=README + '\n\n' + CHANGES,
    url='http://github.com/seedifferently/pytagdump',
    keywords='mutagen ID3',
    packages=[],
    install_requires=['mutagen >= 1.20'],
    extras_require=extras_require,
    scripts=['bin/pytagdump'],
    license = "MIT",
    platforms = "Posix; MacOS X; Windows",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ]
)
