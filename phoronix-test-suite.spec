%define _requires_exceptions pear(.*)

%define name	phoronix-test-suite
%define version 2.4.0b2
%define release %mkrel 1

Summary:	A Comprehensive Linux Benchmarking System
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv3
Group:		Publishing
Url:		http://www.phoronix-test-suite.com/

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
$RPM_BUILD_DIR/%{name}/install-sh $RPM_BUILD_ROOT/usr
sed -i "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT/%{_bindir}/phoronix-test-suite

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%_sysconfdir/bash_completion.d/%name
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%doc %{_datadir}/doc/%{name}
