from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thirvu_event/__init__.py
from thirvu_event import __version__ as version

setup(
	name="thirvu_event",
	version=version,
	description="Thirvu Event",
	author="Thirvusoft",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
