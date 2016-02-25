# $Id$
# Authority: matthias

### libquicktime fails to build with this on EL3
# ExcludeDist: el2 el3
%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_asm 1}
%{?el3:%define _without_glibc232 1}
%{?el3:%define _without_modxorg 1}

%define date 20160221

Summary: Library for encoding and decoding H264/AVC video streams
Name: x264
Version: 0.0.0
Release: 0.4.%{date}%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://developers.videolan.org/x264.html

Source: http://downloads.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-%{date}-2245.tar.bz2
Patch0: x264-20090708-glibc232.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: nasm
BuildRequires: yasm
%{?_with_visualize:%{!?_without_modxorg:BuildRequires: libXt-devel}}
%{?_with_visualize:%{?_without_modxorg:BuildRequires: XFree86-devel}}

Obsoletes: x264-gtk <= %{version}-%{release}

%description
Utility and library for encoding H264/AVC video streams.

%package devel
Summary: Development files for the x264 library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig
Obsoletes: x264-gtk-devel <= %{version}-%{release}

%description devel
This package contains the files required to develop programs that will encode
H264/AVC video streams using the x264 library.

%prep
%setup -n %{name}-snapshot-%{date}-2245
# configure hardcodes X11 lib path
%{__perl} -pi -e 's|/usr/X11R6/lib |/usr/X11R6/%{_lib} |g' configure

### Required for glibc < 2.3.2 (http://article.gmane.org/gmane.comp.video.x264.devel/1696)
%{?_without_glibc232:%patch0 -p0}

%build
# Force PIC as applications fail to recompile against the lib on x86_64 without
./configure \
    --prefix="%{_prefix}" \
    --bindir="%{_bindir}" \
    --includedir="%{_includedir}" \
    --libdir="%{_libdir}" \
%{?_without_asm:--disable-asm} \
    --enable-debug \
    --enable-pic \
    --enable-pthread \
    --enable-static \
    --enable-shared \
%{?_with_visualize:--enable-visualize} \
    --extra-cflags="%{optflags}"
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
%doc AUTHORS COPYING
%{_bindir}/x264
%{_libdir}/libx264.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.txt
%{_includedir}/x264.h
%{_includedir}/x264_config.h
%{_libdir}/pkgconfig/x264.pc
%{_libdir}/libx264.a
%{_libdir}/libx264.so

%changelog
* Tue Feb 23 2016 Moriyoshi Koizumi <mozo@mozo.jp> - 0.0.0-0.4.20160221
- Updated to git release 20160221 (soname .148).

* Mon Nov 15 2010 Dag Wieers <dag@wieers.com> - 0.0.0-0.4.20101111
- Updated to git release 20101111 (soname .107).

* Wed Jul 08 2009 Dag Wieers <dag@wieers.com> - 0.0.0-0.4.20090708
- Updated to git release 20090708 (soname .68).

* Wed May 30 2007 Matthias Saou <http://freshrpms.net/> 0.0.0-0.4.20070529
- Update to 20070529 snasphot for F7 (soname .54 bump to .55).
- Add missing ldconfig calls for the gtk sub-package.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.3.20061214
- Update to 20061214 snapshot (same soname, no rebuilds required).

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.3.20061023
- Update to 20061023 snapshot, the last was too old for MPlayer 1.0rc1.
- Remove no longer needed gtk patch.

* Mon Sep 18 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.2.20060731
- Update to 20060917 snapshot.

* Tue Aug  1 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.2.20060731
- Update to 20060731 snapshot.
- Require the main package from the devel since we have a shared lib now.
- Remove no longer needed symlink patch.
- Enable gtk, include patch to have it build, and split off sub-packages.

* Thu Jun  8 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.2.20060607
- Switch to using the official snapshots.
- Remove no longer needed UTF-8 AUTHORS file conversion.
- Simplify xorg build requirement.
- Switch from full %%configure to ./configure with options since no autotools.
- Enable shared library at last.
- Add our %%{optflags} to the build.
- Include patch to make the *.so symlink relative.

* Thu Mar 16 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-0.1.svn468
- Update to svn 468.
- Lower version from 0.0.svn to 0.0.0 since one day 0.0.1 might come out,
  this shouldn't be much of a problem since the lib is only statically linked,
  thus few people should have it installed, and build systems which aren't
  concerned about upgrade paths should get the latest available package.

* Thu Feb 23 2006 Matthias Saou <http://freshrpms.net/> 0.0.439-1
- Update to svn 439.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.0.396-2
- Enable modular xorg conditional build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.0.396-1
- Update to svn 396.

* Tue Nov 29 2005 Matthias Saou <http://freshrpms.net/> 0.0.380-2
- Also force PIC for the yasm bits, thanks to Anssi Hannula.

* Tue Nov 29 2005 Matthias Saou <http://freshrpms.net/> 0.0.380-1
- Update to svn 380.
- Force PIC as apps fail to recompile against the lib on x86_64 without.
- Include new pkgconfig file.

* Tue Oct  4 2005 Matthias Saou <http://freshrpms.net/> 0.0.315-1
- Update to svn 315.
- Disable vizualize since otherwise programs trying to link without -lX11 will
  fail (cinelerra in this particular case).

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 0.0.285-1
- Update to svn 285.
- Add yasm build requirement (needed on x86_64).
- Replace X11 lib with lib/lib64 to fix x86_64 build.

* Tue Aug  2 2005 Matthias Saou <http://freshrpms.net/> 0.0.281-1
- Update to svn 281.

* Mon Jul 11 2005 Matthias Saou <http://freshrpms.net/> 0.0.273-1
- Initial RPM release.

