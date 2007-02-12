Summary:	Library implementing the SSH protocol
Summary(pl.UTF-8):   Biblioteka implementująca protokół SSH
Name:		libssh
Version:	0.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://0xbadc0de.be/libssh/%{name}-%{version}.tgz
# Source0-md5:	ad703c4702646c83ca4fcace92c220d3
Patch0:		%{name}-makefile.patch
URL:		http://0xbadc0de.be/wiki/doku.php?id=libssh:libssh
BuildRequires:	autoconf
BuildRequires:	automake
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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libssh
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libssh library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libssh.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
