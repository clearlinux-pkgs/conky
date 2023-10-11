#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : conky
Version  : 1.19.5
Release  : 13
URL      : https://github.com/brndnmtthws/conky/archive/v1.19.5/conky-1.19.5.tar.gz
Source0  : https://github.com/brndnmtthws/conky/archive/v1.19.5/conky-1.19.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: conky-bin = %{version}-%{release}
Requires: conky-data = %{version}-%{release}
Requires: conky-lib = %{version}-%{release}
Requires: conky-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : glibc-dev
BuildRequires : imlib2-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libmicrohttpd)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pangofc)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Vim filetype detection and syntax highlighting scripts for conky.
Individual users can place them your personal .vim directory:

%package bin
Summary: bin components for the conky package.
Group: Binaries
Requires: conky-data = %{version}-%{release}
Requires: conky-license = %{version}-%{release}

%description bin
bin components for the conky package.


%package data
Summary: data components for the conky package.
Group: Data

%description data
data components for the conky package.


%package doc
Summary: doc components for the conky package.
Group: Documentation

%description doc
doc components for the conky package.


%package lib
Summary: lib components for the conky package.
Group: Libraries
Requires: conky-data = %{version}-%{release}
Requires: conky-license = %{version}-%{release}

%description lib
lib components for the conky package.


%package license
Summary: license components for the conky package.
Group: Default

%description license
license components for the conky package.


%prep
%setup -q -n conky-1.19.5
cd %{_builddir}/conky-1.19.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697034261
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DBUILD_PORT_MONITORS=OFF -DBUILD_LUA_CAIRO=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBUILD_PORT_MONITORS=OFF -DBUILD_LUA_CAIRO=ON
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697034261
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conky
cp %{_builddir}/conky-%{version}/3rdparty/toluapp/COPYRIGHT %{buildroot}/usr/share/package-licenses/conky/9dcaf12014ad45c0f3a231eeda56550b1a4f094e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/conky
/usr/bin/conky

%files data
%defattr(-,root,root,-)
/usr/share/applications/conky.desktop
/usr/share/icons/hicolor/scalable/apps/conky-logomark-violet.svg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/conky-1.19.5_pre/conky.conf
/usr/share/doc/conky-1.19.5_pre/conky_no_x11.conf
/usr/share/doc/conky-1.19.5_pre/convert.lua

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/conky/libcairo.so
/usr/lib64/conky/libcairo.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conky/9dcaf12014ad45c0f3a231eeda56550b1a4f094e
