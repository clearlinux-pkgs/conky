#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : conky
Version  : 1.12.2
Release  : 9
URL      : https://github.com/brndnmtthws/conky/archive/v1.12.2/conky-1.12.2.tar.gz
Source0  : https://github.com/brndnmtthws/conky/archive/v1.12.2/conky-1.12.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: conky-bin = %{version}-%{release}
Requires: conky-data = %{version}-%{release}
Requires: conky-lib = %{version}-%{release}
Requires: conky-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-scons
BuildRequires : glibc-dev
BuildRequires : imlib2-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xlib)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libmicrohttpd)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(librsvg-2.0)

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
%setup -q -n conky-1.12.2
cd %{_builddir}/conky-1.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619751391
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_PORT_MONITORS=OFF -DBUILD_LUA_CAIRO=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1619751391
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/conky
cp %{_builddir}/conky-1.12.2/3rdparty/toluapp/COPYRIGHT %{buildroot}/usr/share/package-licenses/conky/9dcaf12014ad45c0f3a231eeda56550b1a4f094e
cp %{_builddir}/conky-1.12.2/LICENSE %{buildroot}/usr/share/package-licenses/conky/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/conky

%files data
%defattr(-,root,root,-)
/usr/share/applications/conky.desktop
/usr/share/icons/hicolor/scalable/apps/conky-logomark-violet.svg

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/conky-1.12.2_pre/conky.conf
/usr/share/doc/conky-1.12.2_pre/conky_no_x11.conf
/usr/share/doc/conky-1.12.2_pre/convert.lua

%files lib
%defattr(-,root,root,-)
/usr/lib64/conky/libcairo.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/conky/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/conky/9dcaf12014ad45c0f3a231eeda56550b1a4f094e
