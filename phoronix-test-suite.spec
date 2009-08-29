%define name	phoronix-test-suite
%define version 2.0.0
%define release %mkrel 1

Summary:	A Comprehensive Linux Benchmarking System
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3
Group:		Publishing
Url:		http://www.phoronix-test-suite.com/

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	php-cli
Requires:	php-gtk2

Suggest:	freeimage-devel
Suggest:	ftjam
Suggest:	git
Suggest:	gcc-gfortran
Suggest:	glew-devel
Suggest:	gtk+2-devel
Suggest:	java
Suggest:	libopenjpeg-devel
Suggest:	imlib2-devel
Suggest:	libaio-devel
Suggest:	libcurl-devel
Suggest:	libfftw-devel
Suggest:	libpopt-devel
Suggest:	libvorbis-devel
Suggest:	openal-devel
Suggest:	perl-devel
#Suggest:	perl-opengl # will be needed in a further revision but we are too close of the release
Suggest:	portaudio-devel
Suggest:	png-devel
Requires:	php-cli
Suggest:	php-gd
Suggest:	scons
Suggest:	SDL-devel
Suggest:	SDL_gfx-devel
Suggest:	SDL_net-devel
Suggest:	SDL_image-devel
Suggest:	SDL_sound-devel
Suggest:	SDL_ttf-devel
Suggest:	task-c-devel
Suggest:	task-c++-devel
Suggest:	tcsh
Suggest:	X11-devel

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
