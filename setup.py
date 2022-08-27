from pathlib import Path

from setuptools import find_packages, setup

SETUP_DIRECTORY = Path(__file__).resolve().parent

with (SETUP_DIRECTORY / "README.md").open() as ifs:
    LONG_DESCRIPTION = ifs.read()

install_requires = (
    [
        "you-get>=0.4.1620",
    ],
)

setup(
    name="biliget",
    version="0.0.1",
    author="Yin Cheng",
    author_email="yin.sjtu@gmail.com",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/yinsn/biliget",
    python_requires=">=3.7",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    include_package_data=True,
)
