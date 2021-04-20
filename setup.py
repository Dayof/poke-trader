import io
import re

from setuptools import find_packages, setup

with io.open('./src/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

prod = []
dev = ['pytest', 'pycodestyle', 'coverage', 'isort' 'ipdb']

db = ['pymongo', 'flask_pymongo', 'flask_mongoengine', 'mongoengine']
base = ['requests', 'pathlib', 'flask_cors', 'click', 'flask', 'tqdm']

setup(
    name="poketrader",
    version=version,
    author='Dayanne Fernandes',
    author_email='dayannefernandesc@gmail.com',
    packages=find_packages(exclude='tests'),
    long_description=long_description,
    description="Poke trader.",
    install_requires=[*base, *db],
    entry_points={
        'console_scripts': [
            'poketrader = src.main:start',
            'poketrader-db = src.main:db_start'
        ],
    },
    extras_require={
        'dev': dev,
        'prod': prod
    },
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7'
    ],
    keywords=(
        'Pokemon'
    )
)
