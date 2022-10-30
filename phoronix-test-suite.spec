%global __requires_exclude pear\\(.*\\)

Summary:	A Comprehensive Linux Benchmarking System
Name:		phoronix-test-suite
Version:	10.8.4
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
Requires:	php-posix
Requires:	php-curl
Requires:	php-pcntl
Requires:	php-sockets

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
%autosetup -n %{name} -p1

# fix non-executable-script
chmod +x pts-core/external-test-dependencies/scripts/install-macports-packages.sh
chmod +x pts-core/static/sample-pts-client-update-script.sh

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
Categories=GTK;System;Monitor;
EOF

%post
%systemd_post phoromatic-client.service
%systemd_post phoromatic-server.service
%systemd_post phoronix-result-server.service

%postun
%systemd_postun_with_restart phoromatic-client.service
%systemd_postun_with_restart phoromatic-server.service
%systemd_postun_with_restart phoronix-result-server.service

%preun
%systemd_preun phoromatic-client.service
%systemd_preun phoromatic-server.service
%systemd_preun phoronix-result-server.service

%files
%doc %{_datadir}/doc/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_unitdir}/*.service
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_iconsdir}/hicolor/*/*/*.png
%doc %{_mandir}/man1/%{name}.1*
