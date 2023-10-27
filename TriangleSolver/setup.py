from setuptools import setup

APP = ['trianglesolver.py']
DATA_FILES = ['background.png','solution.jpg']
OPTIONS = {
 'iconfile':'triangle.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
