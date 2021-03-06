# $Id$
# Authority: dries
# Upstream: Paul Evans <leonerd$leonerd,org,uk>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FCGI-Async

Summary: Module to allow use of FastCGI asynchronously
Name: perl-FCGI-Async
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI-Async/

Source: http://www.cpan.org/modules/by-module/FCGI/FCGI-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::HexString)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(Encode)
BuildRequires: perl(IO::Async::Listener) >= 0.23
BuildRequires: perl(IO::Async::Loop) >= 0.16
BuildRequires: perl(IO::Async::Test)
# http://rt.cpan.org/Public/Bug/Display.html?id=48119
Provides: perl(FCGI::Async::BuildParse)
Provides: perl(FCGI::Async::ClientConnection)
Provides: perl(FCGI::Async::Constants)

%description
Module to allow use of FastCGI asynchronously.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml examples/
%doc %{_mandir}/man3/FCGI::Async.3pm*
%doc %{_mandir}/man3/FCGI::Async::*.3pm*
%dir %{perl_vendorlib}/FCGI/
%{perl_vendorlib}/FCGI/Async/
%{perl_vendorlib}/FCGI/Async.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.17-1
- Updated to version 0.17.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.16-1
- Updated to version 0.16.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
