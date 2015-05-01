#!/bin/bash

VERSION=$(python setup.py --version)

git commit -m "release v$VERSION"
git tag $VERSION -m "v$VERSION"
git push --tags
python setup.py sdist upload -r pypi
sudo pip install agileid --upgrade
