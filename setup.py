from setuptools import setup, find_packages
import os


def read(*paths):
    """Read the contents of a text file safely
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="lazydm",
    version="0.1.0",
    description="Tools for lazy DMs",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Francocontigo",
    python_requires=">=3.12",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
    },
)
