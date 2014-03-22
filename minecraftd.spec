%define  pkgver	1.7.2

Name:           minecraftd
Version:    	0.0.2    
Release:        1%{?dist}
Summary:       	systemd service for minecraft server 

License:	GPL        
URL:     	http://minecraft.net/       
Source0:        https://s3.amazonaws.com/Minecraft.Download/versions/%{pkgver}/minecraft_server.%{pkgver}.jar
BuildArch: 	noarch
BuildRequires:	coreutils	  
Requires:      	java, systemd, screen, expect

%description
Installs a minectraft server

%prep
cp -p %SOURCE0 .
cp -p ~/rpmbuild/SOURCES/minecraftd .
cp -p ~/rpmbuild/SOURCES/minecraftd-diag .
cp -p ~/rpmbuild/SOURCES/minecraftd.service .
cp -p ~/rpmbuild/SOURCES/minecraftctl .
cp -p ~/rpmbuild/SOURCES/conf.minecraft .
cp -p ~/rpmbuild/SOURCES/minecraft-server.install .


%install
rm -rf $RPM_BUILD_ROOT

install -Dm744 minecraftd $RPM_BUILD_ROOT/usr/bin/minecraftd
install -Dm744 minecraftd-diag $RPM_BUILD_ROOT/usr/bin/minecraftd-diag
install -Dm744 minecraftctl $RPM_BUILD_ROOT/usr/bin/minecraftctl
mkdir -p $RPM_BUILD_ROOT/srv/minecraft/
install -Dm644 minecraft_server.%{pkgver}.jar $RPM_BUILD_ROOT/srv/minecraft/minecraft_server.jar
install -Dm644 minecraftd.service $RPM_BUILD_ROOT/usr/lib/systemd/system/minecraftd.service
install -Dm644 conf.minecraft $RPM_BUILD_ROOT/etc/conf.d/minecraft
mkdir -p $RPM_BUILD_ROOT/srv/minecraft/backup 

%post
  getent group "minecraft" &>/dev/null || groupadd -r minecraft 1>/dev/null
  getent passwd "minecraft" &>/dev/null || useradd -r -g minecraft -d "/srv/minecraft" -s "/bin/bash" minecraft 1>/dev/null
  touch /srv/minecraft/server.log
  chown -R minecraft:minecraft "/srv/minecraft" 1>/dev/null
  ln -s /srv/minecraft/server.log /var/log/minecraft.log
  systemctl enable minecraftd.service

  cat << EOF
==> World data is stored under /srv/minecraft
==> The server runs as "minecraft", not root
==> You can access the server's console as root with:
      $ screen -r minecraft
==> The systemd service is called "minecraftd.service"
==> Calling "stop" or "restart" with systemctl will gracefully exit the server, saving world data
==> Modify /etc/conf.d/minecraft to change the invocation of the server if you wish
==> A script at /usr/bin/minecraftctl is also provided. See the wiki for details on its usage.

 
EOF


%files
/usr/bin/minecraftd
/usr/bin/minecraftd-diag
/usr/bin/minecraftctl
/srv/minecraft/minecraft_server.jar
/usr/lib/systemd/system/minecraftd.service
/etc/conf.d/minecraft


%doc

%changelog
* Wed Mar 19 2014 magnus
- 
