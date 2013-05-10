### MD TODO rename src pkg dir to hfsplus
%define major	0
%define libname %mklibname hfsp %{major}
%define devname %mklibname hfsp -d

Summary:	User-space HFS+ utilities
Name:		hfsplus
Version:	1.0.4
Release:	11
License:	GPLv2
Group:		File tools
Url:		http://penguinppc.org/files/users/hasi/
Source0:	%{name}_%{version}.src.tar.bz2
Patch0:		hfsplus-1.0.4-debian_jumbo_patch.diff
Patch1:		hfsplus-1.0.4-automake-fix.patch
Patch2:		hfsplus-automake-1.13.patch

%description
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%package utils
Summary:	User-space HFS+ utilities
Group:		File tools
Provides:	hfsplusutils = %{version}-%{release}
Obsoletes:	hfsplusutils < 1.0.4-11

%description utils
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%package -n	%{libname}
Summary:	User-space HFS+ library
Group:		System/Libraries
Obsoletes:	%{_lib}hfsplusutils0 < 1.0.4-11

%description -n	%{libname}
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%package -n	%{devname}
Summary:	User-space HFS+ utilities development files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}hfsplusutils0-devel < 1.0.4-11

%description -n	%{devname}
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%prep
%setup -q
%apply_patches

%build
libtoolize --copy --force
aclocal
autoheader
automake -c -a -f
autoconf
%configure2_5x \
	--disable-static

%make CFLAGS="%{optflags}"

%install
%makeinstall

%files utils
%doc doc/bugs.html doc/faq.html doc/hfsp.html doc/libhfsp.html doc/man/hfsp.sgml
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libhfsp.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so

