Name:             python-saharaclient
Version:          XXX
Release:          XXX
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


Requires:         python-iso8601
Requires:         python-requests
Requires:         python-six
Requires:         python-setuptools
Requires:         python-babel
Requires:         python-netaddr


%description
Python client library for interacting with OpenStack Sahara API.


%prep
%setup -q -n %{name}-%{upstream_version}

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
# TODO mimccune fix up unittests
# sh run_tests.sh --no-virtual-env --no-pep8

%files
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/sahara
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info


%changelog
