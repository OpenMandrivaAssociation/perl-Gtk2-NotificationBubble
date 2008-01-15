%define module NotificationBubble

Summary: Perl module interface to the EggNotificationBubble library
Name:    perl-Gtk2-%module
Version: 0.01
Release: %mkrel 7
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

