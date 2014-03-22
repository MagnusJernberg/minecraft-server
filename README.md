minecraft-server
================

Creates a Linux RPM package that sets up a systemd-ready minecraft server

To install:
1. Clone the git repository
2. sudo yum install fedora-packager (or make sure that 'rpmbuild' is installed
3. execute #rpmdev-setuptree
4. execute biuld.sh
5. sudo yum install ~/rpmbuild/RPMS/noarch/minecraftd-"version".noarch.rpm
6. systemctl start minecraftd.service

And then you have your service up and running.
