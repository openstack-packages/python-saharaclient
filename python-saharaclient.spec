Name:             python-saharaclient
Version:          0.7.0
Release:          1%{?dist}
Provides:         python-savannaclient = %{version}-%{release}
Obsoletes:        python-savannaclient <= 0.5.0-2
Summary:          Client library for OpenStack Sahara API
License:          ASL 2.0
URL:              https://launchpad.net/sahara
Source0:          http://tarballs.openstack.org/python-saharaclient/python-saharaclient-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-d2to1
BuildRequires:    python-pbr >= 0.5.19
# Needed by check
BuildRequires:    python-hacking
BuildRequires:    python-coverage >= 3.6
BuildRequires:    mock >= 1.0
BuildRequires:    python-docutils >= 0.9.1
BuildRequires:    python-oslo-sphinx
BuildRequires:    python-testrepository >= 0.0.15
BuildRequires:    python-sphinx


Requires:         python-iso8601
Requires:         python-requests
Requires:         python-six
Requires:         python-setuptools
Requires:         python-babel
Requires:         python-netaddr


%description
Python client library for interacting with OpenStack Sahara API.


%prep
%setup -q -n %{name}-%{version}
rm -rf python_saharaclient.egg-info
rm -rf test-requirements.txt


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%check
# Building on koji with virtualenv requires test-requirements.txt and this
# causes errors when trying to resolve the package names, also turning on pep8
# results in odd exceptions from flake8.
sh run_tests.sh --no-virtual-env --no-pep8

%files
%doc LICENSE ChangeLog README.rst
%{_bindir}/sahara
%{python_sitelib}/saharaclient
%{python_sitelib}/*.egg-info


%changelog
* Thu Apr  3 2014 Michael McCune <mimccune@redhat> - 0.7.0-1
- 0.7.0 release and rename from python-savannaclient

* Sat Mar  1 2014 Matthew Farrellee <matt@redhat> - 0.5.0-1
- 0.5.0 release

* Fri Jan 17 2014 Matthew Farrellee <matt@redhat> - 0.4.1-1
- 0.4.1 release - introduced Savanna CLI

* Sun Oct 20 2013 Matthew Farrellee <matt@redhat> - 0.3-1
- 0.3 release

* Fri Oct 11 2013 Matthew Farrellee <matt@redhat> - 0.3-0.2
- 0.3 rc3 build

* Sat Aug 17 2013 Matthew Farrellee <matt@redhat> - 0.3-0.1.f816386git
- Initial package
