Summary:	A memory tester
Name:		memtest86
Version:	2.5
Release:	1
URL:		http://reality.sgi.com/cbrady_denver/%{name}/
Source0:	http://reality.sgi.com/cbrady_denver/%{name}/%{name}-%{version}.tar.gz
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems.  BIOS based memory tests are only a quick check and often miss
failures that are detected by Memtest86.

%prep
%setup -q

%build
%{__make} CCFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}" SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot
cp memtest.bin $RPM_BUILD_ROOT/boot/memtest86
gzip -9nf README

%files
%defattr(644,root,root,755)
/boot/memtest86
%doc README*

%clean
rm -rf $RPM_BUILD_ROOT
