from setuptools import setup, find_packages
from cd_sql.version import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cd_sql",
    version=__version__,
    author="Code Docta",
    author_email="codedocta@gmail.com",
    description="This Python package provides a simple and intuitive wrapper for SQLAlchemy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://codedocta.com',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy==2.0.23',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/codedocta/cd_sql/issues',
        'Source': 'https://github.com/codedocta/cd_sql/',
    },
)


