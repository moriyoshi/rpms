# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

### It is included in upstream's perl package
# Tag: rfx

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Builder-Tester

Summary: Test testsuites that have been built with Test::Builder
Name: perl-Test-Builder-Tester
Version: 1.01
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Builder-Tester/

Source: http://www.cpan.org/modules/by-module/Test/Test-Builder-Tester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test testsuites that have been built with Test::Builder.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml
%exclude %{_mandir}/man3/Test::Builder::Tester.3pm*
%exclude %{_mandir}/man3/Test::Builder::Tester::*.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Builder/
%dir %{perl_vendorlib}/Test/Builder/Tester/
%{perl_vendorlib}/Test/Builder/Tester/
%{perl_vendorlib}/Test/Builder/Tester.pm

%changelog
* Tue Mar 22 2011 Yury V. Zaytsev <yury@shurup.com> - 1.01-2
- Fixed man conflict and RFX (thanks to Seán O'Sullivan).

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
