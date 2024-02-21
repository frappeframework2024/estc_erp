from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in estc_erp/__init__.py
from estc_erp import __version__ as version

setup(
	name="estc_erp",
	version=version,
	description="estc_erp",
	author="ESTC",
	author_email="ESTC@mail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
