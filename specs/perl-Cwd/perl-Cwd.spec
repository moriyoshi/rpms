# $Id$

# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define real_name Cwd
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Get the pathname of the current working directory
Name: perl-Cwd
Version: 2.21
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cwd/

Source: http://www.cpan.org/modules/by-module/Cwd/Cwd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This small module getś the pathname of the current working directory.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/auto/Cwd/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.21-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 2.21-1
- Updated to release 2.21.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.20-1 - #%{lastrevid}
- Initial package.
