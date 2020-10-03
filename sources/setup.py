from setuptools import setup

setup(
	name = "mathtools",
	version = "alpha",
	author = "Vivien WALTER",
	author_email = "walter.vivien@gmail.com",
	description = (
	"Collection of tools for mathematics applications in Python"
	),
	license = "GPL3.0",
	packages=[
	'mathtools',
	'mathtools.fit',
	'mathtools.functions',
	'mathtools.plot',
	]
	,
	install_requires=[
	'numpy',
	'pandas',
	'scipy'
	]
)
