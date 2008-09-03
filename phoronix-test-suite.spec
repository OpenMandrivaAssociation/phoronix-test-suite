%define name	phoronix-test-suite
%define version 1.2.0
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

Requires:	freeimage-devel
Requires:	git
Requires:	gcc-gfortran
Requires:	glew-devel
Requires:	gtk+2-devel
Requires:	java
Requires:	jpeg-devel
Requires:	imlib2-devel
Requires:	libaio-devel
Requires:	portaudio-devel
Requires:	png-devel
Requires:	php-cli
Requires:	php-gd
Requires:	scons
Requires:	SDL-devel
Requires:	SDL_gfx-devel
Requires:	SDL_net-devel
Requires:	SDL_image-devel
Requires:	SDL_sound-devel
Requires:	SDL_ttf-devel
Requires:	task-c-devel
Requires:	task-c++-devel
Requires:	tcsh
Requires:	X11-devel


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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%doc %{_datadir}/doc/%{name}
