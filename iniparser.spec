Summary:	C library for parsing "INI-style" files
Summary(pl.UTF-8):	Biblioteka C do analizy plików INI
Name:		iniparser
Version:	4.2.4
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ndevilla/iniparser/tags
Source0:	https://github.com/ndevilla/iniparser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2b4b70171712895cb5afdf1247a8889f
URL:		https://github.com/ndevilla/iniparser
BuildRequires:	cmake >= 3.18
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iniParser is an ANSI C library to parse "INI-style" files, often used
to hold application configuration information.

%description -l pl.UTF-8
iniParser to biblioteka ANSI C do analizy plików w stylu INI, zwykle
używanych do przechowywania informacji o konfiguracji aplikacji

%package devel
Summary:	Header files for iniParser library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki iniParser
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for iniParser library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do biblioteki iniParser.

%package static
Summary:	Static iniParser library
Summary(pl.UTF-8):	Biblioteka statyczna iniParser
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static iniParser library.

%description static -l pl.UTF-8
Biblioteka statyczna iniParser.

%package apidocs
Summary:	API documentation for iniParser library
Summary(pl.UTF-8):	Dokumentacja API biblioteki iniParser
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for iniParser library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki iniParser.

%prep
%setup -q

%build
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS FAQ-en.md LICENSE README.md
%lang(zh_CN) %doc FAQ-zhcn.md
%attr(755,root,root) %{_libdir}/libiniparser.so.*.*.*
%ghost %{_libdir}/libiniparser.so.4

%files devel
%defattr(644,root,root,755)
%{_libdir}/libiniparser.so
%{_includedir}/iniparser
%{_pkgconfigdir}/iniparser.pc
%{_libdir}/cmake/iniparser

%files static
%defattr(644,root,root,755)
%{_libdir}/libiniparser.a

%files apidocs
%defattr(644,root,root,755)
%doc build/html/{search,*.css,*.html,*.js,*.png}
