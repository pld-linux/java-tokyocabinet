Summary:	Java binding for Tokyo Cabinet
Summary(pl.UTF-8):	Wiązania Javy do biblioteki Tokyo Cabinet
Name:		java-tokyocabinet
Version:	1.24
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Java
Source0:	http://fallabs.com/tokyocabinet/javapkg/tokyocabinet-java-%{version}.tar.gz
# Source0-md5:	cb7db713865cedf255916691daa522d2
Patch0:		%{name}-buildenv.patch
URL:		http://fallabs.com/tokyocabinet/
BuildRequires:	bzip2-devel
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	tokyocabinet-devel >= 1.0.3
BuildRequires:	zlib-devel
Requires:	jpackage-utils
Requires:	tokyocabinet-libs >= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tokyo Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of a
key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. There is neither concept of data tables nor data types.
Records are organized in hash table, B+ tree, or fixed-length array.

This package contains Java binding for the library.

%description -l pl.UTF-8
Tokyo Cabinet to biblioteka procedur do zarządzania bazą danych. Baza
danych to prosty plik danych zawierający pary klucz-wartość. Każdy
klucz oraz wartość to szereg bajtów o zmiennej długości. Jako kluczy
oraz wartości można używać zarówno danych binarnych, jak i łańcuchów
znaków. Nie ma konceptu tabel danych ani typów danych. Rekordy są
zorganizowane w tablicy haszującej, B+ drzewie lub tablicy o stałej
długości.

Ten pakiet zawiera wiązania Javy do biblioteki.

%prep
%setup -q -n tokyocabinet-java-%{version}
%patch0 -p1

%build
export JAVA_HOME="%{java_home}"

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/*.jar $RPM_BUILD_ROOT%{_javadir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libjtokyocabinet.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libjtokyocabinet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjtokyocabinet.so.1
%{_javadir}/tokyocabinet.jar
