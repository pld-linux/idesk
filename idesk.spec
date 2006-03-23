Summary:	Idesk allows You to create desktop icons
Summary(pl):	Idesk umo�liwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.7.5
Release:	1
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

%description -l pl
Idesk umo�liwia tworzenie ikon na pulpicie - cecha przydatna, ale nie
oferowana przez wszystkich zarz�dc�w okien. Grafiki ikon pochodz� z
plik�w PNG lub (wektorowych) SVG i wspieraj� niekt�re efekty takie
jak przezroczysto��. Ka�da ikona mo�e by� skonfigurowana do
uruchamiania jednego lub wi�kszej liczby polece� pow�oki, a akcje
uruchamiaj�ce te polecenia s� w pe�ni konfigurowalne.

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
