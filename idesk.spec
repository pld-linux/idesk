Summary:	Idesk allows You to create desktop icons
Summary(pl.UTF-8):	Idesk umożliwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.7.5
Release:	2
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/idesk/%{name}-%{version}.tar.bz2
# Source0-md5:	beb48c97815c7b085e3b3d601297fbb8
URL:		http://idesk.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Idesk allows creation of desktop icons. Feature quite nice, and not
provided by all window managers. The icon graphics are either from a
PNG or SVG (vector) file and support some eyecandy effects like
transparency. Each icon can be configured to run one or more shell
commands and the actions which run those commands are completely
configurable.

%description -l pl.UTF-8
Idesk umożliwia tworzenie ikon na pulpicie - cecha przydatna, ale nie
oferowana przez wszystkich zarządców okien. Grafiki ikon pochodzą z
plików PNG lub (wektorowych) SVG i wspierają niektóre efekty takie
jak przezroczystość. Każda ikona może być skonfigurowana do
uruchamiania jednego lub większej liczby poleceń powłoki, a akcje
uruchamiające te polecenia są w pełni konfigurowalne.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/idesk
