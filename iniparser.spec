Summary:	C library for parsing "INI-style" files
Name:		iniparser
Version:	3.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://ndevilla.free.fr/iniparser/%{name}-%{version}.tar.gz
# Source0-md5:	0aa4f995468ed390caf323f50a285bc3
URL:		http://ndevilla.free.fr/iniparser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iniParser is an ANSI C library to parse "INI-style" files, often used
to hold application configuration information.

%package devel
Summary:	Header files, libraries and development documentation for %{name}
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and
development documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir} $RPM_BUILD_ROOT%{_libdir}
install -t $RPM_BUILD_ROOT%{_includedir} src/dictionary.h src/iniparser.h
install -t $RPM_BUILD_ROOT%{_libdir}/ libiniparser.so.0
ln -s libiniparser.so.0 $RPM_BUILD_ROOT%{_libdir}/libiniparser.so
install -t $RPM_BUILD_ROOT%{_libdir}/ libiniparser.a


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_libdir}/lib%{name}.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.a
%{_includedir}/*.h
