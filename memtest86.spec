Summary:	A memory tester
Summary(pl):	Tester pamiêci
Name:		memtest86
Version:	2.8a
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.teresaudio.com/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.memtest86.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems. BIOS based memory tests are only a quick check and often miss
failures that are detected by Memtest86.

%description -l pl
Memtest86 jest ci±g³ym, samodzielnym testerem pamiêci dla systemów
architektury i386. Testy pamiêci przez BIOS s± tylko szybkim
sprawdzeniem i zazwyczaj nie wykrywaj± b³êdów znajdywanych przez
memtest86.

%prep
%setup -q -n %{name}-%(echo %{version} | tr -d [:alpha:])

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
