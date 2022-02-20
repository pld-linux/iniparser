Summary:	C library for parsing "INI-style" files
Summary(pl.UTF-8):	Biblioteka C do analizy plików INI
Name:		iniparser
Version:	4.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/ndevilla/iniparser/tags
Source0:	https://github.com/ndevilla/iniparser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e43b722c71b399ab17c329c04dbdf1d7
URL:		http://ndevilla.free.fr/iniparser
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

%description apidocs
API documentation for iniParser library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki iniParser.

%prep
%setup -q

%build
LDFLAGS="%{rpmldflags} %{rpmcflags}" \
%{__make} \
	CC="%{__cc}" \
	ADDITIONAL_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

cp -p src/{dictionary.h,iniparser.h} $RPM_BUILD_ROOT%{_includedir}
install -p libiniparser.so.1 $RPM_BUILD_ROOT%{_libdir}
ln -sf libiniparser.so.1 $RPM_BUILD_ROOT%{_libdir}/libiniparser.so
cp -p libiniparser.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS FAQ-en.md LICENSE README.md
%lang(zh_CN) %doc FAQ-zhcn.md
%attr(755,root,root) %{_libdir}/libiniparser.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libiniparser.so
%{_includedir}/dictionary.h
%{_includedir}/iniparser.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libiniparser.a

%files apidocs
%defattr(644,root,root,755)
%doc html/*.{css,html,gif,png}
