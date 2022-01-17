from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gauri/__init__.py
from gauri import __version__ as version

setup(
	name="gauri",
	version=version,
	description="test",
	author="test",
	author_email="sgkads",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
