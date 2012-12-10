%define version 2.4
%define release	1

Summary:	Graphics puzzle similar to Rubik's cube
Name:		gnubik
Version:	%{version}
Release:	%{release}
License:	GPLv3+
Group:		Games/Puzzles
URL:		http://www.gnu.org/software/gnubik/

Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Patch2:		gnubik-2.4-printf.patch
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtkglext-devel
BuildRequires:	gtk+2.0

%description
GNUbik is a GNU package.  It is a 3D interactive graphics 
puzzle. It renders an image of a magic cube 
(similar to a rubik cube) and you attempt to solve it.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --with-widget-set=gtk
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name} 
Icon=puzzle_section 
Comment=Puzzle game similar to Rubik's cube 
Categories=Game;LogicGame;
Name=Gnubik
EOF
rm %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%{name}
%{_infodir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3-4mdv2011.0
+ Revision: 610951
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2010.1
+ Revision: 437790
- rebuild

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 2.3-2mdv2009.1
+ Revision: 364134
- fix desktop file

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 2.3-1mdv2009.1
+ Revision: 336395
- New version 2.3

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.2-4mdv2009.0
+ Revision: 246488
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.2-2mdv2008.1
+ Revision: 132153
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gnubik


* Mon Mar 21 2005 Abel Cheung <deaddog@mandrake.org> 2.2-2mdk
- Rebuild

* Sun Feb 27 2005 Abel Cheung <deaddog@mandrake.org> 2.2-1mdk
- First Mandrakelinux package
