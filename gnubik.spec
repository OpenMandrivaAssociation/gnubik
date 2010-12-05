%define version 2.3
%define release  %mkrel 4

Summary:	Graphics puzzle similar to Rubik's cube
Name:		gnubik
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Puzzles
URL:		http://www.gnu.org/software/gnubik/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:		gnubik-2.3-fix-str-fmt.patch
Patch1:		gnubik-2.3-linkage.patch
BuildRequires:	guile-devel >= 1.6.4
BuildRequires:	gtkglext-devel

%description
GNUbik is a GNU package.  It is a 3D interactive graphics 
puzzle. It renders an image of a magic cube 
(similar to a rubik cube) and you attempt to solve it.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --with-widget-set=gtk
%make

%install
rm -rf %{buildroot}
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

%find_lang %{name}

%post
%if %mdkversion < 200900
%update_menus
%endif
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%{name}
%{_infodir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
