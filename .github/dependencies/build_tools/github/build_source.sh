#!/bin/bash

set -e
set -x

# Move up two levels to create the virtual
# environment outside of the source folder
# cd ../../

python -m venv build_env
source build_env/bin/activate
pwd
cd /home/runner/work/PKNSETools/PKNSETools/
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
pip3 install .
python -m pip install setuptools twine wheel build

# python3 setup.py clean build sdist bdist_wheel
python -m build --sdist

# Check whether the source distribution will render correctly
twine check dist/*.tar.gz