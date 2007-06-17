# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Carp-Assert-More

Summary: Convenience wrappers around Carp::Assert 
Name: perl-Carp-Assert-More
Version: 1.12
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Carp-Assert-More/

Source: http://www.cpan.org/modules/by-module/Carp/Carp-Assert-More-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Convenience wrappers around Carp::Assert.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Carp/
%dir %{perl_vendorlib}/Carp/Assert/
%{perl_vendorlib}/Carp/Assert/More.pm

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
