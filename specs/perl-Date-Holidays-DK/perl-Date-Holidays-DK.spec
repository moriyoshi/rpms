# $Id$
# Authority: dries
# Upstream: Lars Thegler <lars$thegler,dk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Holidays-DK

Summary: Determines whether a given date is a Danish public holiday or not
Name: perl-Date-Holidays-DK
Version: 0.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Holidays-DK/

Source: http://search.cpan.org/CPAN/authors/id/L/LT/LTHEGLER/Date-Holidays-DK-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Date::Holidays::DK Determines whether a given date is a Danish public holiday
or not.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Date/Holidays/DK.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.

