# $Id$
# Authority: dries
# Upstream: Tye McQueen <tyemq$cpan,org>

%define real_name Algorithm-Diff
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Compute intelligent differences between two files or lists
Name: perl-Algorithm-Diff
Version: 1.1901
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-Diff/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-Diff-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a module for computing the difference between two files, two
strings, or any other two lists of things.  It uses an intelligent
algorithm similar to (or identical to) the one used by the Unix "diff"
program.  It is guaranteed to find the *smallest possible* set of
differences.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Algorithm/

%changelog
* Fri Jan  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.1901-1
- Initial package.
