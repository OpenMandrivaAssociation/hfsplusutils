%define major 0
%define libname %mklibname %{name} %{major}

Summary:	User-space HFS+ utilities
Name:		hfsplusutils
Version:	1.0.4
Release:	%mkrel 8
License:	GPL
Group:		File tools
URL:		http://penguinppc.org/files/users/hasi/
Source0:	hfsplus_%{version}.src.tar.bz2
Patch0:		hfsplus-1.0.4-debian_jumbo_patch.diff
Patch1:		hfsplus-1.0.4-automake-fix.patch
BuildRequires:	automake1.8
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%package -n	%{libname}
Summary:	User-space HFS+ library
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{libname}
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%package -n	%{libname}-devel
Summary:	User-space HFS+ utilities development files
Group:		Development/Other
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
A portable, free implementation of routines for accessing HFS+ volumes.
Currently only reading is supported.

%prep

%setup -q -n hfsplus-%{version}
%patch0 -p1
%patch1 -p1 -b .automake-fix

%build
libtoolize --copy --force
aclocal-1.8
autoheader
automake-1.8 -c -a -f
autoconf
%configure2_5x

%make CFLAGS="%{optflags}"

%install
rm -fr %{buildroot}

%makeinstall

%clean
rm -fr %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc doc/bugs.html doc/faq.html doc/hfsp.html doc/libhfsp.html doc/man/hfsp.sgml
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


