Summary:	Idesk allows You to create desktop icons
Summary(pl):	Idesk umo¿liwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.7.3
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/idesk/%{name}-%{version}.tar.gz
# Source0-md5:	c4afb05492f1ec87b0d2be210e228681
URL:		http://idesk.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Idesk allows creation of desktop icons. Feature quite nice, and not
provided by all window managers. The icon graphics are either from a
png or svg (vector) file and support some eyecandy effects like
transparency. Each icon can be confgured to run one or more shell
commands and the actions which run those commands are completely
configurable.

%description -l pl
Idesk umo¿liwia tworzenie ikon na pulpicie - cecha przydatna, ale nie
oferowana przez wszystkie window managery.

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
