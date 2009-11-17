Summary:	Library implementing the SSH protocol
Summary(pl.UTF-8):	Biblioteka implementująca protokół SSH
Name:		libssh
Version:	0.4.0
Release:	0.git.1
Epoch:		1
License:	LGPL
Group:		Libraries
#Source0:	http://www.libssh.org/files/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-git.tar.gz
# Source0-md5:	0c8db6b22944b0d4f50d3d3dbdf646ae
URL:		http://www.libssh.org/
BuildRequires:	cmake >= 2.6.0
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	zlib-devel
BuildRequires:	doxygen
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-makeindex
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
%setup -q -n %{name}-%{version}-git

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?

%files devel
%defattr(644,root,root,755)
%{_libdir}/libssh.so
%{_includedir}/libssh
