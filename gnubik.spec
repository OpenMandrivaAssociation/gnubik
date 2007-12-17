%define version 2.2
%define release  %mkrel 2

Summary:	Graphics puzzle similar to Rubik's cube
Name:		gnubik
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Puzzles
URL:		http://www.gnu.org/software/gnubik/

Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig

BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtkglext-devel

%description
GNUbik is a GNU package.  It is a 3D interactive graphics 
puzzle. It renders an image of a magic cube 
(similar to a rubik cube) and you attempt to solve it.

%prep
%setup -q

%build
%configure2_5x --with-widget-set=gtk
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_menudir}
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application << _EOF_
Exec=%{_bindir}/%{name} 
Icon=puzzle_section 
Comment=Puzzle game similar to Rubik's cube 
Categories=Game;LogicGame; 
Name=Gnubik
EOF

# only 1 french translation exists, and french is not
# very different across countries, so use it as the main
# translation
mv %{buildroot}%{_datadir}/locale/{fr_FR,fr}

%find_lang %{name}

%post
%update_menus
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_infodir}/*

%{_datadir}/applications/mandriva-%{name}.desktop

