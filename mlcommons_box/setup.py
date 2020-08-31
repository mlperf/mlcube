from setuptools import find_packages, setup
import os

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

def schemas():
    paths = []
    for (path, _, filenames) in os.walk("mlcommons_box/schemas"):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths

extra_files = schemas()

setup(
    name="mlcommons_box",
    version="0.1",
    packages=find_packages(exclude=["tests"]),
    entry_points='''
        [console_scripts]
        mlcommons_box=mlcommons_box.main:cli
    ''',
    install_requires=requires,
    package_data={"": extra_files},
    extras_require={},
)
