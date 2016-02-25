# $Id$
# Authority: matthias

Summary: Library for encoding and decoding AAC audio streams
Name: fdk-aac
Version: 0.1.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: https://github.com/mstorsjo/fdk-aac

Source: http://downloads.sourceforge.net/project/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: yasm
BuildRequires: cmake

%description
Utility and library for encoding and decoding AAC audio streams.

%package devel
Summary: Development files for the fdk-aac library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the files required to develop programs that will encode
or decode AAC audio streams using the fdk-aac library.

%prep
%setup -n %{name}-%{version}
# configure hardcodes X11 lib path
%{__perl} -pi -e 's|/usr/X11R6/lib |/usr/X11R6/%{_lib} |g' configure

%build
%configure --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc NOTICE
%{_libdir}/libfdk-aac.so.*

%files devel
%defattr(-, root, root, 0755)
%doc documentation/aacDecoder.pdf documentation/aacEncoder.pdf
%{_includedir}/fdk-aac/*.h
%{_libdir}/pkgconfig/fdk-aac.pc
%{_libdir}/libfdk-aac.a
%{_libdir}/libfdk-aac.so
%{_libdir}/libfdk-aac.la

%changelog
* Tue Feb 23 2016 Moriyoshi Koizumi <mozo@mozo.jp> 0.1.4-1
- Initial RPM release.
