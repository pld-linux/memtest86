Summary:	A memory tester
Name:		memtest86
Version:	2.7
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://reality.sgi.com/cbrady_denver/%{name}/%{name}-%{version}.tar.gz
URL:		http://reality.sgi.com/cbrady_denver/%{name}/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems. BIOS based memory tests are only a quick check and often miss
failures that are detected by Memtest86.

%prep
%setup -q

%build
%{__make} CCFLAGS="%{rpmcflags}" SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot

%{__install} memtest.bin $RPM_BUILD_ROOT/boot/memtest86

gzip -9nf README

%files
%defattr(644,root,root,755)
%doc *.gz
/boot/memtest86

%clean
rm -rf $RPM_BUILD_ROOT
