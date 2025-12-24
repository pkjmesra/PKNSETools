# -*- coding: utf-8 -*-
# """
#     The MIT License (MIT)

#     Copyright (c) 2023 pkjmesra

#     Permission is hereby granted, free of charge, to any person obtaining a copy
#     of this software and associated documentation files (the "Software"), to deal
#     in the Software without restriction, including without limitation the rights
#     to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#     copies of the Software, and to permit persons to whom the Software is
#     furnished to do so, subject to the following conditions:

#     The above copyright notice and this permission notice shall be included in all
#     copies or substantial portions of the Software.

#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#     AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#     OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#     SOFTWARE.

# """
"""
Spyder Editor

This is a temporary script file.

python setup.py clean build install sdist bdist_wheel

"""
# import atexit, os
import sys
import os
import shutil
from distutils.core import setup

import setuptools  # noqa

from PKNSETools import __version__ as VERSION

__USERNAME__ = 'pkjmesra'
# Package name must be lowercase (normalized) for PyPI compliance
# The actual package directory is still PKNSETools for backward compatibility
__PACKAGENAME__ = 'pknsetools'
__PACKAGE_DIR__ = 'PKNSETools'  # Actual directory name

install_requires=[]
if os.path.exists("README.md") and os.path.isfile("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
if os.path.exists("requirements.txt") and os.path.isfile("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        install_requires = fh.read().splitlines()
elif os.path.exists(os.path.join(__PACKAGE_DIR__,"requirements.txt")) and os.path.isfile(os.path.join(__PACKAGE_DIR__,"requirements.txt")):
    with open(os.path.join(__PACKAGE_DIR__,"requirements.txt"), "r", encoding="utf-8") as fh:
        install_requires = fh.read().splitlines()


SYS_MAJOR_VERSION = str(sys.version_info.major)
SYS_VERSION = SYS_MAJOR_VERSION + "." + str(sys.version_info.minor)

WHEEL_NAME = (
    __PACKAGENAME__ + "-" + VERSION + "-py" + SYS_MAJOR_VERSION + "-none-any.whl"
)
TAR_FILE = __PACKAGENAME__ + "-" + VERSION + ".tar.gz"
EGG_FILE = __PACKAGENAME__ + "-" + VERSION + "-py" + SYS_VERSION + ".egg"
DIST_FILES = [WHEEL_NAME, TAR_FILE, EGG_FILE]
DIST_DIR = "dist/"

# def _post_build():
# 	if "bdist_wheel" in sys.argv:
# 		for count, filename in enumerate(os.listdir(DIST_DIR)):
# 			if filename in DIST_FILES:
# 				os.rename(DIST_DIR + filename, DIST_DIR + filename.replace(__PACKAGENAME__+'-', __PACKAGENAME__+'_'+__USERNAME__+'-'))

# atexit.register(_post_build)

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

package_files_To_Install = ["LICENSE","README.md","requirements.txt"]
package_files = [__PACKAGE_DIR__ + ".ini","courbd.ttf"]
package_dir_path = os.path.join(os.getcwd(), __PACKAGE_DIR__)
if os.path.exists(package_dir_path):
    for file in package_files_To_Install:
        targetFileName = file.split(os.sep)[-1].split(".")[0] + ".txt"
        package_files.append(targetFileName)
        srcFile = os.path.join(os.getcwd(),file)
        if os.path.isfile(srcFile):
            shutil.copy(srcFile,os.path.join(package_dir_path,targetFileName))

setup(
	name = __PACKAGENAME__,
	packages=setuptools.find_packages(where=".", exclude=["docs", "test"]),
    cmdclass={'bdist_wheel': bdist_wheel},
	include_package_data = True,    # include everything in source control
	package_data={__PACKAGE_DIR__: ["release.md"],"":package_files},
	# ...but exclude README.txt from all packages
	exclude_package_data = { '': ['*.yml'] },
	version = VERSION,
	description = 'A Python-based data downloader for NSE, India',
	long_description = long_description,
	long_description_content_type="text/markdown",
	author = __USERNAME__,
	author_email = __USERNAME__+'@gmail.com',
	license = 'OSI Approved (MIT)',
	url = 'https://github.com/'+__USERNAME__+'/PKNSETools', # use the URL to the github repo
	zip_safe=False,
	# entry_points='''
	# [console_scripts]
	# PKNSETools=PKNSETools.PKNSEToolscli:PKNSEToolscli
	# pkbot=PKNSETools.PKNSEToolsbot:main
	# ''',
	download_url = 'https://github.com/'+__USERNAME__+'/PKNSETools/archive/v' + VERSION + '.zip',
	classifiers=[
	"License :: OSI Approved :: MIT License",
	"Operating System :: Microsoft :: Windows",
	"Operating System :: MacOS",
	"Operating System :: POSIX :: Linux",
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
	],
	install_requires = install_requires,
	keywords = ['NSE', 'Stocks','Data Download'],
	test_suite="test",
),
python_requires='>=3.12',
