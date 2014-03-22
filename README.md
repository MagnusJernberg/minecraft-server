minecraft-server
================

Creates a Linux RPM package that sets up a systemd-ready minecraft server

To install:
* Clone the git repository
* sudo yum install fedora-packager (or make sure that 'rpmbuild' is installed
* execute #rpmdev-setuptree
* execute biuld.sh
* sudo yum install ~/rpmbuild/RPMS/noarch/minecraftd-"version".noarch.rpm
* systemctl start minecraftd.service

And then you have your service up and running.
