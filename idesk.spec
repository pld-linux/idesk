Summary:	Idesk allows You to create desktop icons
Summary(pl):	Idesk umo¿liwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.7.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/idesk/%{name}-%{version}.tar.gz
# Source0-md5:	b78fd6a1dba16ae0c29d0c3b7b3c2f1c
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
provided by all window managers.

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
%doc ChangeLog COPYING README TODO
%attr(755,root,root) %{_bindir}/*
