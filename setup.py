from setuptools import setup, find_packages

setup(
    name="advent-of-code-blackfisch",
    version="0.1",
    description="blackfisch's solutions for https://adventofcode.com/",
    url="https://github.com/blackfisch/advent-of-code-blackfisch",
    author="Rico Goldhardt",
    author_email="blackfisch@outlook.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 1.2.2",
        "importlib"
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["blackfisch = aoc_blackfisch:solve"],
    },
)
