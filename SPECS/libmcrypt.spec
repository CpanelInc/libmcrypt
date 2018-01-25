%define ns_prefix ea
%define pkg_base  libmcrypt
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{pkg_base}

Summary:   libmcrypt is a data encryption library.
Name:      %{pkg_name}
Version:   2.5.8
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4554 for more details
%define release_prefix 5
Release: %{release_prefix}%{?dist}.cpanel
License:   LGPL
Source:    ftp://mcrypt.hellug.gr/pub/crypto/mcrypt/%{pkg_base}-%{version}.tar.gz
Vendor:    cPanel, Inc.
Group:     System Environment/Libraries

%description
libmcrypt is a data encryption library. The library is thread safe
and provides encryption and decryption functions. This version of the
library supports many encryption algorithms and encryption modes. Some
algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more.

%package devel
Summary: Development files of the libmcrypt data encryption library.
Group: Development/Libraries
Requires: %{pkg_name} = %{version}

%description devel
Header file and static libraries of libmcrypt data encryption library.

%prep
%setup -n %{pkg_base}-%{version}

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --disable-dependency-tracking \
    --disable-maintainer-mode

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p ${RPM_BUILD_ROOT}/%{_docdir}

%check
make check

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
ldconfig

%postun
ldconfig

%files
/opt/cpanel/libmcrypt

#%defattr(-, root, root, 0755)

%files devel
#%defattr(-, root, root, 0755)
%dir %{_docdir}
%doc doc/README* doc/example.c AUTHORS ChangeLog KNOWN-BUGS NEWS
%doc THANKS README TODO
%{_libdir}/libmcrypt.la
%{_includedir}/mcrypt.h
%{_includedir}/mutils/mcrypt.h
%{_prefix}/man/man3/mcrypt.*
%{_bindir}/libmcrypt-config
%{_datadir}/aclocal/libmcrypt.m4

%changelog
* Tue Jan 23 2018 Dan Muey <dan@cpanel.net> - 2.5.8-5
- EA-7136: Add root path to %files and Ensure ownership of %{_docdir}

* Fri Dec 16 2016 Cory McIntire <cory@cpanel.net> - 2.5.8-4
- Updated Vendor field

* Mon Jun 20 2016 Dan Muey <dan@cpanel.net> - 2.5.8-3
- EA-4383: Update Release value to OBS-proof versioning

* Tue Aug 11 2015 Trinity Quirk <trinity.quirk@cpanel.net> - 2.5.8-2
- Renamed to ea-libmcrypt
- Moved into /opt/cpanel

* Thu Aug 06 2015 Trinity Quirk <trinity.quirk@cpanel.net> - 2.5.8-1
- Repaired for cPanel distribution

* Tue Dec 17 2002 Germano Rizzo <mano@pluto.linux.it>
- modified for new installation structure

* Fri Feb 01 2002 Germano Rizzo <mano@pluto.linux.it>
- built basing on Peter Soos' SPEC file

* Mon Oct 01 2001 Peter Soos  <sp@osb.hu>
- rebuilt under RedHat Linux 7.2 beta
- version 2.4.17

* Fri May 04 2001 Peter Soos  <sp@osb.hu>
- rebuilt under RedHat Linux 7.1

* Wed Apr 18 2001 Peter Soos <sp@osb.hu>
- RedHat Linux 7.0

* Thu Feb 15 2001 Peter Soos <sp@osb.hu>
- version 2.4.9

* Thu Nov 02 2000 Peter Soos <sp@osb.hu>
- version 2.4.5

* Fri Jun 23 2000 Peter Soos <sp@osb.hu>
- version 2.4.4

* Sun Nov 07 1999 Peter Soos <sp@osb.hu>
- Separate this package from the mcrypt package
