%define _requires_exceptions pear(.*)

# GUI was temporary dropped since 3.0 Aplha 1
%define		gui_enabled 0

Name:		phoronix-test-suite
Version:	3.8.0
Release:	1
Summary:	A Comprehensive Linux Benchmarking System
Source0:	%{name}-%{version}.tar.gz
Patch0:		phoronix-test-suite-3.6.1-install.patch
License:	GPLv3
Group:		Publishing
Url:		http://www.phoronix-test-suite.com/

BuildArch:	noarch

Requires:	php-cli
Requires:	php-gtk2
Requires:	php-fpdf

Suggests:	freeimage-devel
Suggests:	ftjam
Suggests:	git
Suggests:	gcc-gfortran
Suggests:	glew-devel
Suggests:	gtk+2-devel
Suggests:	java
Suggests:	libopenjpeg-devel
Suggests:	imlib2-devel
Suggests:	libaio-devel
Suggests:	libcurl-devel
Suggests:	libfftw-devel
Suggests:	libpopt-devel
Suggests:	libvorbis-devel
Suggests:	openal-devel
Suggests:	perl-devel
#Suggests:	perl-opengl # will be needed in a further revision but we are too close of the release
Suggests:	portaudio-devel
Suggests:	png-devel
Suggests:	php-gd
Suggests:	scons
Suggests:	SDL-devel
Suggests:	SDL_gfx-devel
Suggests:	SDL_net-devel
Suggests:	SDL_image-devel
Suggests:	SDL_sound-devel
Suggests:	SDL_ttf-devel
Suggests:	task-c-devel
Suggests:	task-c++-devel
Suggests:	tcsh
Suggests:	X11-devel

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking 
platform available for Linux and is designed to carry out qualitative and 
quantitative benchmarks in a clean, reproducible, and easy-to-use manner.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
echo "fake build"

%install
%__mkdir_p %{buildroot}%{_prefix}
./install-sh %{buildroot}%{_prefix}
%__sed -i "s|%{buildroot}||g" %{buildroot}%{_bindir}/%{name}

%if %{gui_enabled}
# we overwrite default desktop file with the better one
# should be checked if it's needed when GUI is back
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Phoronix Test Suite
Comment=Phoronix Test Suite Benchmarking Utility
Exec=%{_bindir}/%{name} gui
Icon=%{name}
Terminal=false
Type=Application
Encoding=UTF-8
StartupNotify=true
Categories=GTK;System;Monitor;X-MandrivaLinux-CrossDesktop;
EOF
%endif

%files
%defattr(-,root,root,0755)
%doc %{_datadir}/doc/%{name}
%{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/phoronix-test-suite-launcher.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
