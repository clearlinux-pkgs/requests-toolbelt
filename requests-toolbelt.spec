#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-toolbelt
Version  : 0.9.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/28/30/7bf7e5071081f761766d46820e52f4b16c8a08fef02d2eb4682ca7534310/requests-toolbelt-0.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/30/7bf7e5071081f761766d46820e52f4b16c8a08fef02d2eb4682ca7534310/requests-toolbelt-0.9.1.tar.gz
Summary  : A utility belt for advanced users of python-requests
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-toolbelt-license = %{version}-%{release}
Requires: requests-toolbelt-python = %{version}-%{release}
Requires: requests-toolbelt-python3 = %{version}-%{release}
Requires: requests
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
The Requests Toolbelt
=====================
This is just a collection of utilities for `python-requests`_, but don't
really belong in ``requests`` proper. The minimum tested requests version is
``2.1.0``. In reality, the toolbelt should work with ``2.0.1`` as well, but
some idiosyncracies prevent effective or sane testing on that version.

%package license
Summary: license components for the requests-toolbelt package.
Group: Default

%description license
license components for the requests-toolbelt package.


%package python
Summary: python components for the requests-toolbelt package.
Group: Default
Requires: requests-toolbelt-python3 = %{version}-%{release}

%description python
python components for the requests-toolbelt package.


%package python3
Summary: python3 components for the requests-toolbelt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the requests-toolbelt package.


%prep
%setup -q -n requests-toolbelt-0.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548817780
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-toolbelt
cp LICENSE %{buildroot}/usr/share/package-licenses/requests-toolbelt/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-toolbelt/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
