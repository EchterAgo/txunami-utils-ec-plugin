#!/bin/sh

here=$(dirname $(realpath "$0" 2> /dev/null || grealpath "$0"))
plugname=txunami-utils
version=$(git describe --tags)
outfile="$here/$plugname-$version.zip"

cd "$here"
zip -9 "$outfile" -@ << EOF
manifest.json
txunami-utils/__init__.py
txunami-utils/qt.py
EOF
cd -

exit 0
