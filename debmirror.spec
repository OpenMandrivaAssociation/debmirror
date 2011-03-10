%define name	debmirror
%define version 2.7
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:      1
Summary:	Debian partial mirror script, with ftp and package pool support
License:	GPL or Artistic
Group:		Development/Other
Url:		http://packages.debian.org/unstable/net/debmirror
Source:		http://ftp.debian.org/debian/pool/main/d/debmirror/%{name}_%{version}.tar.gz
Buildarch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This program downloads and maintains a partial local Debian mirror. It can
mirror any combination of architectures, distributions and sections. Files are
transferred by ftp, http, hftp or rsync, and package pools are fully supported.
It also does locking and updates trace files.

%prep
%setup -q -n debmirror

%build
pod2man debmirror debmirror.1

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 debmirror %{buildroot}%{_bindir}
install -m 755 mirror-size %{buildroot}%{_bindir}
install -m 644 debmirror.1 %{buildroot}%{_mandir}/man1

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc doc/* debian/NEWS debian/copyright debian/changelog examples
%{_bindir}/*
%{_mandir}/man1/*

