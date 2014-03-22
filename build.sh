#!/bin/sh

whereami=$(dirname $0)

if [ ! -f "$(which rpmdev-setuptree)" ]; then echo "please install '@development-tools' and 'fedora-packager' rpm and try again" ; exit 1 ; fi

# creates ~/rpmbuild
/usr/bin/rpmdev-setuptree

cp -f ${whereami}/minecraftd.spec ~/rpmbuild/SPECS/
cp -f ${whereami}/* ~/rpmbuild/SOURCES/
/usr/bin/spectool -C ~/rpmbuild/SOURCES/ -g ${whereami}/minecraftd.spec

rpmbuild -bb ~/rpmbuild/SPECS/minecraftd.spec


