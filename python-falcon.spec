%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

Name:           python-falcon
Version:        0.1.8
Release:        1%{?dist}
Summary:        A supersonic micro-framework for building cloud APIs

License:        ASL 2.0
Group:          Development/Libraries
URL:            http://falconframework.org
Source0:        https://pypi.python.org/packages/source/f/falcon/falcon-%{version}.tar.gz

Requires:       python-six
Requires:       python-mimeparse

BuildRequires:  Cython
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-testtools

%description
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.

Features:
- Intuitive routing via URI templates and resource classes
- Easy access to headers and bodies through request and response classes
- Idiomatic HTTP error responses via a handy exception base class
- DRY request processing using global, resource, and method hooks
- Snappy unit testing through WSGI helpers and mocks
- 20% speed boost when Cython is available
- Python 2.6, Python 2.7, PyPy and Python 3.3 support
- Speed, speed, and more speed!

%if 0%{?with_python3}
%package -n python3-falcon
Summary:        A supersonic micro-framework for building cloud APIs
Requires:       python3-mimeparse
Requires:       python3-six

BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-testtools

%description -n python3-falcon
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.

Features:
- Intuitive routing via URI templates and resource classes
- Easy access to headers and bodies through request and response classes
- Idiomatic HTTP error responses via a handy exception base class
- DRY request processing using global, resource, and method hooks
- Snappy unit testing through WSGI helpers and mocks
- 20% speed boost when Cython is available
- Python 2.6, Python 2.7, PyPy and Python 3.3 support
- Speed, speed, and more speed!
%endif

%prep
%setup -q -n falcon-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif

# don't package the benchmark test
rm $RPM_BUILD_ROOT/%{_bindir}/falcon-bench

%check
%{__python2} setup.py test

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES.md LICENSE NOTES.md README.rst
%{python2_sitearch}/falcon
%{python2_sitearch}/falcon-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-falcon
%doc AUTHORS CHANGES.md LICENSE NOTES.md README.rst
%{python3_sitearch}/falcon
%{python3_sitearch}/falcon-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Feb 27 2014 Jamie Lennox <jamielennox@redhat.com> - 0.1.8-1
- Bump to 0.1.8

* Mon Sep 23 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Add Python 3 packaging details and patch to fix for Python 3.
- Remove falcon-bench from package.
- Added check section.

* Wed Sep 18 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Initial package.
