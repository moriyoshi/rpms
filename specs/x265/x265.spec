# $Id$
# Authority: matthias

Summary: Library for encoding H265/HEVC video streams
Name: x265
Version: 1.9
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://developers.videolan.org/x265.html

Source: http://downloads.videolan.org/pub/videolan/x265/x265_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: yasm
BuildRequires: cmake

%description
Utility and library for encoding H265/HEVC video streams.

%package devel
Summary: Development files for the x265 library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
This package contains the files required to develop programs that will encode
H265/HEVC video streams using the x265 library.

%prep
%setup -n %{name}_%{version}
# configure hardcodes X11 lib path
%{__perl} -pi -e 's|/usr/X11R6/lib |/usr/X11R6/%{_lib} |g' configure

%build
# Force PIC as applications fail to recompile against the lib on x86_64 without
cd build/linux
%cmake -G "Unix Makefiles" \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    %{?_without_asm:-DENABLE_ASSENBLY=OFF} \
    ../../source

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd build/linux
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_bindir}/x265
%{_libdir}/libx265.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/reST/*.rst
%{_includedir}/x265.h
%{_includedir}/x265_config.h
%{_libdir}/pkgconfig/x265.pc
%{_libdir}/libx265.a
%{_libdir}/libx265.so

%changelog
* Tue Feb 23 2016 Moriyoshi Koizumi <mozo@mozo.jp> 1.9-1
- Initial RPM release.

