Summary:	Graphics puzzle similar to Rubik's cube
Name:		gnubik
Version:	2.4
Release:	3
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
%autopatch -p1

%build
%configure2_5x --with-widget-set=gtk
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

# Replace defalt desktop file
rm %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 755 %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name} 
Icon=puzzle_section 
Comment=Puzzle game similar to Rubik's cube 
Comment[ru]=Головоломка, похожая на кубик Рубика 
Categories=Game;LogicGame;
Name=Gnubik
Name[ru]=Gnubik
EOF

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%{name}
%{_infodir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*


