%define name	debmirror
%define version 20060907
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Debian partial mirror script, with ftp and package pool support
License:	GPL or Artistic
Group:		Development/Other
Source:		ftp.debian.org/debian/pool/main/d/debmirror/%{name}_%{version}.1.tar.bz2
Url:		http://packages.debian.org/unstable/net/debmirror
BuildRequires:  perl
Buildarch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This program downloads and maintains a partial local Debian mirror. It can
mirror any combination of architectures, distributions and sections. Files are
transferred by ftp, http, hftp or rsync, and package pools are fully supported.
It also does locking and updates trace files.

%prep
%setup -q -n %{name}-20060908

%build
pod2man debmirror debmirror.1

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 debmirror %{buildroot}%{_bindir}
install -m 644 debmirror.conf %{buildroot}%{_sysconfdir}
install -m 644 debmirror.1 %{buildroot}%{_mandir}/man1

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc doc/* Makefile.* NEWS.Debian
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf

