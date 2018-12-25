%global __requires_exclude pear\\(.*\\)

Summary:	A Comprehensive Linux Benchmarking System
Name:		phoronix-test-suite
Version:	8.4.1
Release:	1
License:	GPLv3
Group:		Publishing
Url:		http://www.phoronix-test-suite.com/
Source0:	http://www.phoronix-test-suite.com/releases/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	php-cli
Requires:	php-gd
Requires:	php-xml
Requires:	php-dom
Requires:	php-openssl
Requires:	php-sqlite3
Requires:	php-json
Requires:	php-posix
Requires:	php-curl
Requires:	php-pcntl
Requires:	php-sockets
Requires:	rpm-helper

Recommends:	freeimage-devel
Recommends:	ftjam
Recommends:	git
Recommends:	gcc-gfortran
Recommends:	java
Recommends:	libaio-devel
Recommends:	perl-devel
Recommends:	perl-OpenGL
Recommends:	pkgconfig(fftw3)
Recommends:	pkgconfig(glew)
Recommends:	pkgconfig(gtk+-2.0)
Recommends:	pkgconfig(imlib2)
Recommends:	pkgconfig(libcurl)
Recommends:	pkgconfig(libopenjpeg1)
Recommends:	pkgconfig(libpng)
Recommends:	pkgconfig(openal)
Recommends:	pkgconfig(popt)
Recommends:	pkgconfig(portaudio-2.0)
Recommends:	pkgconfig(sdl)
Recommends:	pkgconfig(SDL_gfx)
Recommends:	pkgconfig(SDL_net)
Recommends:	pkgconfig(SDL_image)
Recommends:	pkgconfig(SDL_ttf)
Recommends:	pkgconfig(vorbis)
Recommends:	pkgconfig(x11)
Recommends:	SDL_sound-devel
Recommends:	scons
Recommends:	task-c-devel
Recommends:	task-c++-devel
Recommends:	tcsh

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking
platform available for Linux and is designed to carry out qualitative and
quantitative benchmarks in a clean, reproducible, and easy-to-use manner.

%prep
%setup -q -n %{name}

# fix non-executable-script
chmod +x pts-core/external-test-dependencies/scripts/install-macports-packages.sh
chmod +x pts-core/static/sample-pts-client-update-script.sh
chmod -x pts-core/objects/phodevi/sensors/network_usage.php

%build

%install
export DESTDIR=%{buildroot}
./install-sh %{_prefix}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}-gui.desktop <<EOF
[Desktop Entry]
Name=Phoronix Test Suite (GUI)
GenericName=A GUI for Phoronix Test Suite Benchmarking Utility
GenericName[fr]=Une interface graphique pour l'utilitaire d'évaluation Phoronix Test Suite
Comment=Phoronix Test Suite GUI
Comment[fr]=Interface graphique de Phoronix Test Suite
Exec=%{_bindir}/%{name} gui
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;System;Monitor;X-Mageia-CrossDesktop;
EOF

%post
%_post_service phoromatic-client
%_post_service phoromatic-server

%preun
%_preun_service phoromatic-client
%_preun_service phoromatic-server

%files
%doc %{_datadir}/doc/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
#{_unitdir}/phoromatic-client.service
#{_unitdir}/phoromatic-server.service
/usr/lib/systemd/system/phoromatic-client.service
/usr/lib/systemd/system/phoromatic-server.service
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-launcher.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/64x64/mimetypes/*.png
%{_mandir}/man1/%{name}.1*
