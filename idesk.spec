Summary:	Idesk allows You to create desktop icons
Summary(pl):	Idesk umo¿liwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.5.6
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/idesk/%{name}-%{version}.tar.gz
# Source0-md5:	0a52c8f1d80cbd238edcfd96d937b146
URL:		http://idesk.sourceforge.net/site/
BuildRequires:	gtk+2-devel
BuildRequires:	imlib-devel
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Idesk allows creation of desktop icons. Feature quite nice, and not
provided by all window managers.

%description -l pl
Idesk umo¿liwia tworzenie ikon na pulpicie - cecha przydatna, ale nie
oferowana przez wszystkie window managery.

%prep
%setup -q -c

%build
%{__make} \
	cc="%{__cxx}" \
	cflags="%{rpmcflags} `imlib-config --cflags` `freetype-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install idesk $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
