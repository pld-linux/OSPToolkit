Summary:	Implementation of the ETSI OSP VoIP Peering protocol
Summary(pl.UTF-8):	Implementacja protokołu ETSI OSP VoIP Peering
Name:		OSPToolkit
Version:	4.2.0
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/osp-toolkit/%{name}-%{version}.tar.gz
# Source0-md5:	edb0ac6d84cf6da0f0406f3d356b6204
Patch0:		sharedlib.patch
URL:		http://www.freerouteserver.com/index.php/osp-toolkit
BuildRequires:	openssl-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OSP Toolkit is a complete development kit for software developers
who want to implement the client side of the European
Telecommunication Standards Institute's (ETSI) OSP standard for secure
VoIP peering. The OSP Toolkit includes source code written in ANSI C,
test tools and extensive documentation on how to implement the OSP
peering protocol standard.

%description -l pl.UTF-8
OSP Toolkit to kompletny zestaw programistyczny dla programistów
implementujących kliencką stronę standardu ETSI (European
Telecommunication Standards Institute) OSP dla bezpiecznej komunikacji
VoIP. OSP Toolkit zawiera kod źródłowy w ANSI C, narzędzia testowe
oraz szczegółową dokumentację jak zaimplementować standard OSP
Peering.

%package devel
Summary:	Header files for OSP Toolkit library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OSP Toolkit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OSP Toolkit library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OSP Toolkit.

%package static
Summary:	Static OSP Toolkit library
Summary(pl.UTF-8):	Statyczna biblioteka OSP Toolkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OSP Toolkit library.

%description static -l pl.UTF-8
Statyczna biblioteka OSP Toolkit.

%prep
%setup -q -n TK-%(echo %{version} | tr . _)-20131014
%patch0 -p1
%{__sed} -i -e 's,\$(INSTALL_PATH)/lib,$(INSTALL_PATH)/%{_lib},' src/Makefile

%build
%{__make} -C src build \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	DFLAGS="%{rpmcflags} %{rpmcppflags}"

%{__make} -C enroll linux \
	CC="%{__cc}" \
	DFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

%{__make} -C src install \
	INSTALL_PATH=$RPM_BUILD_ROOT%{_prefix}

chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_libdir}/libosptk.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libosptk.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libosptk.so
%{_includedir}/osp

%files static
%defattr(644,root,root,755)
%{_libdir}/libosptk.a
