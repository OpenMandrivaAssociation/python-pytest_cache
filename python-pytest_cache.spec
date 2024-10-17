# Created by pyp2rpm-2.0.0
%global pypi_name pytest-cache
%global with_python2 0
%define version 1.0

Name:           python-%{pypi_name}
Version:        1.0
Release:        1
Group:          Development/Python
Summary:        This plugin provides two options to rerun failures

License:        MIT
URL:            https://pythonhosted.org/blinker/
Source0:        https://pypi.python.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
This plugin provides two options to rerun failures, namely --lf to only re-run the failures 
and --ff to run all tests but the failures from the last run first. 
For cleanup (usually not needed), a --clearcache option allows removal of all cross-session 
cache contents ahead of a test run.

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        This plugin provides two options to rerun failures

%description -n python2-%{pypi_name}
The plugin provides two options to rerun failures, namely --lf to only re-run the failures 
and --ff to run all tests but the failures from the last run first. 
For cleanup (usually not needed), a --clearcache option allows removal of all cross-session 
cache contents ahead of a test run.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.rst LICENSE CHANGELOG
%{python_sitelib}/*/*
%{python_sitelib}/pytest_cache.py


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst LICENSE CHANGELOG
%{python2_sitelib}/*/*
%{python2_sitelib}/pytest_cache.py
%endif # with_python2

