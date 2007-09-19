Summary:	Implementation of the ETSI OSP VoIP Peering protocol
Summary(pl.UTF-8):	Implementacja protokołu ETSI OSP VoIP Peering
Name:		OSPToolkit
Version:	3.4.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/osp-toolkit/%{name}-%{version}.tar.gz
# Source0-md5:	e9943630934c65d012fb49a820d8b179
URL:		http://www.transnexus.com/OSP%20Toolkit/OSP%20Toolkit.htm
BuildRequires:	openssl-devel
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

%prep
%setup -q -n TK-3_4_1-20070917

%build
%{__make} -C src build \
	CC="%{__cc}" \
	GCCFLAGS="-Wall -D_GNU_SOURCE -fPIC %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

cp -a include/osp $RPM_BUILD_ROOT%{_includedir}
install lib/*.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_libdir}/lib*.a
%{_includedir}/osp
