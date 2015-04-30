#!/bin/bash

VERSION=$(python setup.py --version)

git commit -m "release $VERSION"
git tag $VERSION -m "release $VERSION"
git push --tags
python setup.py sdist upload -r pypi
sudo pip install agileid  --upgrade
