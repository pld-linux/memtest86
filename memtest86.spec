Summary:	A memory tester
Summary(pl):	Tester pamiêci
Name:		memtest86
Version:	3.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.teresaudio.com/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.memtest86.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if ! %(%{__cc} -dumpversion | grep -q '^3\.0' ; echo $?)
%define		optflags	-O
%endif

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
%{__make} CC="%{__cc}" CCFLAGS="%{rpmcflags}" SHELL=/bin/bash

%install
rm -rf 	$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot

install memtest.bin $RPM_BUILD_ROOT/boot/memtest86

%files
%defattr(644,root,root,755)
%doc README
/boot/memtest86

%clean
rm -rf $RPM_BUILD_ROOT
