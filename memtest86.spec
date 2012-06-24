Summary:	Thorough, stand alone memory test for i386 systems
Summary(pl):	Kompleksowy, niezale�ny od OS tester pami�ci dla system�w i386
Summary(pt_BR):	Testador de mem�ria completo e independente para sistemas i386
Summary(ru_RU):	���� ������ ��� x86-�����������
Summary(uk_UA):	���� ���'�Ԧ ��� x86-��Ȧ�������
Name:		memtest86
Version:	3.0
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.memtest86.com/%{name}-%{version}.tar.gz
# Source0-md5:	fade21758538a5468ad9b8509edfde0d
Patch0:		%{name}-vars.patch
Patch1:		%{name}-rover-centrino+c3+amd.patch
Patch2:		%{name}-i686-ld.patch
URL:		http://www.memtest86.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems. BIOS based memory tests are only a quick check and often miss
failures that are detected by Memtest86.

%description -l pl
Memtest86 jest ci�g�ym, samodzielnym testerem pami�ci dla system�w
architektury i386. Testy pami�ci przez BIOS s� tylko szybkim
sprawdzeniem i zazwyczaj nie wykrywaj� b��d�w znajdywanych przez
memtest86.

%description -l pt_BR
Memtest86 � um testador de mem�ria independente (no sentido de que n�o
roda sob um sistema operacional) e completo para sistemas i386.

%description -l ru_RU
Memtest86 -- ���������� � ��������������� ���� ������ ��� x86-������. �� �����
���� �������� ��� � �������� ����� ��� ������ LILO/GRUB, ��� � �������.

���� ���������� �������� "���������� ��������", ���������� ���� �������������
��� ����������� ����� ������. �� ��������� �������� �� "����" BIOS -- ��
����������� ������ �� ������, ��� ��� ��������� ����� ������ �� ���, �������
��������� memtest86.

����� ����� �������������� ��� �������� ����������� ����-�������.

%description -l uk_UA
Memtest86 -- ��������� �� �����Ԧ���� ���� ���'�Ԧ ��� x86-������. ���
���� ���� ������������ �� � ��������� ����� �� ��������� LILO/GRUB, ���
� � �������.

���� ����������դ �������� "���������� �����Ӧ�", ���� ��צ� ����
�������Φ��� ��� ��������Φ �������Ħ� �� ���'����. �� ��������� �����
�� "����" BIOS -- צ� ��������� Φ���� �� �������, ���� �� ������ ����
�������� ��ϧ� � ���, �� ��������� memtest86.

����� ���� ����������������� ��� ��������� ��������������ϧ
����-�������.

%prep
%setup -q -n %{name}-%(echo %{version} | tr -d [:alpha:])
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} -fomit-frame-pointer -fno-builtin" \
	SHELL=/bin/sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/boot

install memtest.bin $RPM_BUILD_ROOT/boot/memtest86

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
/boot/memtest86
