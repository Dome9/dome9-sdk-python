from setuptools import setup, find_packages
from dome9 import __version__


def readme():
	with open('README.md') as md:
		return md.read()


setup(name='dome9',
	description='Dome9 sdk module',
	version=__version__,
	long_description=readme(),
	author='dome9 sre team',
	author_email='d9ops@checkpoint.com',
	license='MIT',
	url='git+https://github.com/Dome9/dome9-sdk-python',
	packages=find_packages(),
	include_package_data=True,
	install_requires=['requests', 'loguru', 'dataclasses-json'],
	zip_safe=False)
project_urls = {
	"Repository": "https://github.com/Dome9/dome9-sdk-python",
	"Bug Reports": "https://github.com/Dome9/dome9-sdk-python/issues",
	"Documentation": "https://github.com/Dome9/dome9-sdk-python",
},
