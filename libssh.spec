Summary:	Library implementing the SSH protocol
Summary(pl):	Biblioteka implementuj±ca protokó³ SSH
Name:		libssh
Version:	0.2
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://0xbadc0de.be/libssh/%{name}-%{version}.tgz
# Source0-md5:	8a76c03579a3e27046e6bafe88ffd171
URL:		http://0xbadc0de.be/wiki/doku.php?id=libssh:libssh
BuildRequires:	libmagic-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ssh library was designed to be used by programmers needing a
working SSH implementation by the mean of a library. The complete
control of the client is made by the programmer. With libssh, you can
remotely execute programs, transfer files, use a secure and
transparent tunnel for your remote programs. With its Secure FTP
implementation, you can play with remote files easily, without
third-party programs others than libcrypto (from openssl).

%description -l pl
Biblioteka ssh zosta³a zaprojektowana do u¿ywania przez programistów
potrzebuj±cych dzia³aj±cej implementacji SSH w postaci biblioteki. Za
pomoc± libssh mo¿na przesy³aæ pliki, zdalnie uruchamiaæ programy b±d¼
te¿ tworzyæ na ich potrzeby bezpieczne i przezroczyste tunele. Dziêki
zawartej implementacji protoko³u Secure FTP programista ma mo¿liwo¶æ
³atwego wykonywania operacji na zdalnych plikach bez konieczno¶ci
korzystania z dodatkowego zewnêtrznego oprogramowania poza bibliotek±
libcrypto (pakiet openssl).

%package devel
Summary:	Header files for libssh library
Summary(pl):	Pliki nag³ówkowe biblioteki libssh
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libssh library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libssh.

%prep
%setup -q

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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

%files devel
%defattr(644,root,root,755)
%{_libdir}/libssh.so
%{_includedir}/*
