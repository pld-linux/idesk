# TODO: pass optflags
Summary:	Idesk allows You to create desktop icons
Summary(pl):	Idesk umo¿liwia tworzenie ikon na pulpicie
Name:		idesk
Version:	0.3.5
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://linuxhelp.hn.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
URL:		http://linuxhelp.hn.org/idesk.php
BuildRequires:	Xft-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Idesk allows creation of desktop icons. Feature quite nice, and not
provided by all window managers.

%description -l pl
Idesk umo¿liwia tworzenie ikon na pulpicie - cecha przydatna, ale nie
oferowana przez wszystkie window managery.

%prep
%setup -q 
%patch0 -p1

%build
%{__make}

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
