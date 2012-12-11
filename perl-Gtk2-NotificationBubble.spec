%define module NotificationBubble

Summary: Perl module interface to the EggNotificationBubble library
Name:    perl-Gtk2-%module
Version: 0.01
Release:	14
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  Gtk2-%module-%version.tar.bz2
Patch0:  Gtk2-NotificationBubble-0.01-triangle.patch
URL:     http://cvs.gnome.org/viewcvs/rhythmbox/widgets/eggnotificationbubble.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel perl-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib >= 0.92
BuildRequires: perl-Gtk2
BuildRequires: glitz-devel
Requires: gtk+2 perl-Gtk2 >= 0.95-6mdk

%description
This module allows a Perl developer to display notification bubbles on
top of Gtk2 widgets. They look like tooltips with bevelled borders and
arrows. They can display an icon and a bold header.

%prep
%setup -q -n Gtk2-%module-%version
perl Makefile.PL INSTALLDIRS=vendor
%patch0 -p1 -b .triangle

%build
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc examples/*
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/*



%changelog
* Wed Jan 25 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.01-14
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.01-13
+ Revision: 676882
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.01-12
+ Revision: 667187
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.01-11mdv2011.0
+ Revision: 564484
- rebuild for perl 5.12.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.01-10mdv2011.0
+ Revision: 426480
- rebuild

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-9mdv2009.0
+ Revision: 287783
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.01-7mdv2008.1
+ Revision: 152108
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.01-6mdv2008.0
+ Revision: 44533
- cleanups

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-5mdv2008.0
+ Revision: 23406
- rebuild


* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-4mdk
- Fix BuildRequires

* Wed Aug 24 2005 Olivier Blin <oblin@mandriva.com> 0.01-3mdk
- Patch0: fix triangle offset when bubble is on extreme right

* Wed Aug 24 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.01-2mdk
- rebuild with new gtk+

* Fri Aug 19 2005 Olivier Blin <oblin@mandriva.com> 0.01-1mdk
- initial binding

