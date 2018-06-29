#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : offlineimap
Version  : 7.2.1
Release  : 21
URL      : https://github.com/OfflineIMAP/offlineimap/archive/v7.2.1.tar.gz
Source0  : https://github.com/OfflineIMAP/offlineimap/archive/v7.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: offlineimap-bin
Requires: offlineimap-license
Requires: offlineimap-python
Requires: offlineimap-legacypython
Requires: six
Requires: six-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-legacypython

%description
Documentation for the OfflineImap Test suite.
How to run the tests
====================

%package bin
Summary: bin components for the offlineimap package.
Group: Binaries
Requires: offlineimap-license

%description bin
bin components for the offlineimap package.


%package legacypython
Summary: legacypython components for the offlineimap package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the offlineimap package.


%package license
Summary: license components for the offlineimap package.
Group: Default

%description license
license components for the offlineimap package.


%package python
Summary: python components for the offlineimap package.
Group: Default

%description python
python components for the offlineimap package.


%prep
%setup -q -n offlineimap-7.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530274244
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/offlineimap
cp COPYING %{buildroot}/usr/share/doc/offlineimap/COPYING
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/offlineimap

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/offlineimap/COPYING

%files python
%defattr(-,root,root,-)
