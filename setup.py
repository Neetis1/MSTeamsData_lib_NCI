import setuptools
with open("README.md", "r", encoding="utf-8") as fh:long_description = fh.read()
setuptools.setup(
name="MSTeamsdataretrieval_neeti_sharma1",
version="0.0.1",
author="Neeti",
author_email="sharma1992nee@gmail.com",
description="A library to handle MSTeams Attendance report",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/neetrophy/MSTeamsData_lib_NCI",
packages=setuptools.find_packages(),
# if you have libraries that your module/package/library
#you would include them in the install_requires argument
install_requires=[''],
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires='>=3.6',
)
