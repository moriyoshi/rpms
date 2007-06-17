# $Id$

# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$pucrs,br>

%define real_name DateTime-Event-Recurrence
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: DateTime::Set extension for computing basic recurrences
Name: perl-DateTime-Event-Recurrence
Version: 0.16
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-Recurrence/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-Recurrence-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module aims to support basic recurrences, such as 'daily'.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Event/Recurrence.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.
