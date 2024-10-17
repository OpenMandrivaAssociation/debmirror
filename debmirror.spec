%define name	debmirror
%define version 2.7
%define release 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:      1
Summary:	Debian partial mirror script, with ftp and package pool support
License:	GPL or Artistic
Group:		Development/Other
Url:		https://packages.debian.org/unstable/net/debmirror
Source:		http://ftp.debian.org/debian/pool/main/d/debmirror/%{name}_%{version}.tar.gz
Buildarch:  noarch

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
mkdir %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 debmirror %{buildroot}%{_bindir}
install -m 755 mirror-size %{buildroot}%{_bindir}
install -m 644 debmirror.1 %{buildroot}%{_mandir}/man1
install -m 644 examples/debmirror.conf %{buildroot}%{_sysconfdir}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc doc/* debian/NEWS debian/copyright debian/changelog examples
%config(noreplace) %{_sysconfdir}/debmirror.conf
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.7-1mdv2011.0
+ Revision: 643453
- new version

* Sat Aug 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.4.4-1mdv2011.0
+ Revision: 567317
- update to new version 2.4.4

* Sun Jan 24 2010 Frederik Himpe <fhimpe@mandriva.org> 1:2.4.1-1mdv2010.1
+ Revision: 495524
- update to new version 2.4.1

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.4-1mdv2010.1
+ Revision: 483999
- update to new version 2.4

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.3.1-1mdv2010.1
+ Revision: 462313
- update to new version 2.3.1
- Fix source URL

* Thu Sep 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.1.1-1mdv2010.0
+ Revision: 437325
- new version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20070123-1mdv2010.0
+ Revision: 373837
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 20060907-5mdv2009.0
+ Revision: 244022
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060907-4mdv2009.0
+ Revision: 239582
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20060907-2mdv2008.1
+ Revision: 132419
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import debmirror


* Mon Oct 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 20060907-1mdv2007.1
- first mdv release
