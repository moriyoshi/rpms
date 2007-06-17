# $Id$
# Authority: dries
# Upstream: G&#225;bor Egressy <gabor$vmunix,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Format

Summary: Various subroutines to format text
Name: perl-Text-Format
Version: 0.52
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Format/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GABOR/Text-Format%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Various subroutines to format text.

%prep
%setup -n %{real_name}%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Format.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
