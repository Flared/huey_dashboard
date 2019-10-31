import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fh:
    readme = fh.read()

setup(
    name='task-dashboard',
    version=__import__('task_dashboard').__version__,
    description='Task Dashboard',
    long_description=readme,
    author='Israël Hallé',
    author_email='israel.halle@flare.systems',
    url='http://github.com/Flared/task-dashboard/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
