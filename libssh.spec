Summary:	Library implementing the SSH protocol
Summary(pl.UTF-8):	Biblioteka implementująca protokół SSH
Name:		libssh
Version:	0.9.5
Release:	1
Epoch:		1
License:	LGPL v2.1+; parts are BSD-licensed
Group:		Libraries
Source0:	https://www.libssh.org/files/0.9/%{name}-%{version}.tar.xz
# Source0-md5:	6211e47ba4dfd7f7e9f8a17a601245f4
URL:		http://www.libssh.org/
BuildRequires:	cmake >= 3.3.0
BuildRequires:	heimdal-devel
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel >= 1.2
Requires:	zlib >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ssh library was designed to be used by programmers needing a
working SSH implementation by the mean of a library. The complete
control of the client is made by the programmer. With libssh, you can
remotely execute programs, transfer files, use a secure and
transparent tunnel for your remote programs. With its Secure FTP
implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%description -l pl.UTF-8
Biblioteka ssh została zaprojektowana do używania przez programistów
potrzebujących działającej implementacji SSH w postaci biblioteki. Za
pomocą libssh można przesyłać pliki, zdalnie uruchamiać programy bądź
też tworzyć na ich potrzeby bezpieczne i przezroczyste tunele. Dzięki
zawartej implementacji protokołu Secure FTP programista ma możliwość
łatwego wykonywania operacji na zdalnych plikach bez konieczności
korzystania z dodatkowego zewnętrznego oprogramowania poza biblioteką
libcrypto (pakiet openssl).

%package devel
Summary:	Header files for libssh library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libssh
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libssh library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libssh.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DWITH_SSH1=ON \
	-DWITH_ZLIB=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD ChangeLog README
%attr(755,root,root) %{_libdir}/libssh.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libssh.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libssh.so
%{_includedir}/libssh
%{_pkgconfigdir}/libssh.pc
%{_libdir}/cmake/libssh
