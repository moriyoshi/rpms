%global selinux_variants mls targeted
%global selinux_policyver %(sed -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)

Name:		jobber
Version:	1.0.3
Release:	1%{?dist}
Summary:	A replacement for cron, with sophisticated status-reporting and error-handling.
Group:		System Environment/Daemon
License:	MIT
URL:		https://github.com/dshearer/jobber
Source:		https://github.com/dshearer/jobber/archive/v%{version}.tar.gz
Patch0:		no-phony.patch.diff
Patch1:		no-system-configuration-changes.patch.diff
Patch2:		destdir-is-actually-prefix.patch.diff

BuildRequires:	golang checkpolicy selinux-policy-devel
Requires:	initscripts daemonize selinux-policy >= %{selinux_policyver}

Requires(pre): shadow-utils
Requires(post):   /usr/sbin/semodule, /sbin/restorecon
Requires(postun): /usr/sbin/semodule, /sbin/restorecon
Requires(post,preun): chkconfig

%define		jobber_git_revision 6c8338afee9ff57a14c5fb90f70b9f37ea88b473
%define		debug_package %{nil}

%description
Jobber is a replacement for cron, with sophisticated status-reporting and error-handling.


%package	client
Summary:	jobberd client
Group:		System Environment/Daemon

%description	client
Jobber is a replacement for cron, with sophisticated status-reporting and error-handling.  This package contains a client application for jobberd

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
cd %{_builddir}/jobber-%{version}
PATH=%{_builddir}/jobber-%{version}:$PATH
export PATH
cat <<HERE >git
#!/bin/sh
echo %{jobber_git_revision}
HERE
chmod ogu+rx git
mkdir -p build/src/github.com/dshearer
ln -s ../../../.. build/src/github.com/dshearer/jobber
GOPATH=%{_builddir}/jobber-%{version}/build
export GOPATH
make
(
    cd %{_builddir}/jobber-%{version}/se_policy
    for selinuxvariant in %{selinux_variants}
    do
        make NAME=$selinuxvariant -f /usr/share/selinux/devel/Makefile
        mv jobber.pp jobber.pp.$selinuxvariant
        make NAME=$selinuxvariant -f /usr/share/selinux/devel/Makefile clean
    done
)

%install
cd %{_builddir}/jobber-%{version}
GOPATH=%{_builddir}/jobber-%{version}/build
export GOPATH
install -d %{buildroot}/etc/init.d
install -d %{buildroot}/etc/rc.d/init.d
make install CLIENT_USER=root PREFIX=%{_prefix} DESTDIR=%{buildroot}
sed -e 's#/usr/local#%{_prefix}#' %{buildroot}/etc/init.d/jobber > %{buildroot}/etc/rc.d/init.d/jobber && rm %{buildroot}/etc/init.d/jobber
chmod 0755 %{buildroot}/etc/rc.d/init.d/jobber
for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 %{_builddir}/jobber-%{version}/se_policy/jobber.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/jobber.pp
done

%files
%defattr(-, root, root, 0755)
%doc README.md LICENSE
%config /etc/rc.d/init.d/jobber
%{_prefix}/sbin/jobberd
%{_datadir}/selinux/*/jobber.pp

%files client
%defattr(-, root, root, 0755)
%{_prefix}/bin/jobber

%pre
getent passwd jobber_client >/dev/null || useradd -r -g root -d /var/empty -s /sbin/nologin jobber_client

%post
if getent password jobber_client >/dev/null; then userdel jobber_client; fi
for selinuxvariant in %{selinux_variants}; do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/jobber.pp &> /dev/null || :
done
/sbin/restorecon %{_prefix} || :
/sbin/chkconfig --add jobber
/sbin/chkconfig jobber on

%preun
/sbin/chkconfig --del jobber
if [ -f /var/lock/subsys/jobber ]; then /sbin/service jobber stop >/dev/null; fi

%postun
if [ $1 -eq 0 ]; then
  for selinuxvariant in %{selinux_variants}; do
     /usr/sbin/semodule -s ${selinuxvariant} -r jobber &> /dev/null || :
  done
  /sbin/restorecon %{_prefix} || :
fi

%changelog

* Tue Mar 08 2016 Moriyoshi Koizumi <mozo@mozo.jp> - 1.0.3-1
  Initial RPM release.
