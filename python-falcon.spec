%if 0%{?fedora}
%global with_python3 1
%global _docdir_fmt %{name}
%endif

Name:           python-falcon
Version:        0.3.0
Release:        2%{?dist}
Summary:        A supersonic micro-framework for building cloud APIs

License:        ASL 2.0
Group:          Development/Libraries
URL:            http://falconframework.org
Source0:        https://pypi.python.org/packages/source/f/falcon/falcon-%{version}.tar.gz

# https://github.com/falconry/falcon/pull/558
Patch001:       001-fix_test_cookies.patch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools


%description
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%package -n python2-falcon
Summary:        A supersonic micro-framework for building cloud APIs
BuildRequires:  Cython
BuildRequires:  python-coverage
BuildRequires:  python-ddt
BuildRequires:  python-nose
BuildRequires:  python-requests
BuildRequires:  python-six
BuildRequires:  python-testtools
BuildRequires:  PyYAML
Requires:       python-mimeparse
Requires:       python-six
%{?python_provide:%python_provide python2-falcon}


%description -n python2-falcon
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%if 0%{?with_python3}
%package -n python3-falcon
Summary:        A supersonic micro-framework for building cloud APIs
BuildRequires:  python3-Cython
BuildRequires:  python3-coverage
BuildRequires:  python3-ddt
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-testtools
BuildRequires:  python3-PyYAML
Requires:       python3-mimeparse
Requires:       python3-six
%{?python_provide:%python_provide python3-falcon}


%description -n python3-falcon
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.
%endif


%prep
%setup -q -n falcon-%{version}
%patch001 -p1


%build
%{py2_build}
%if 0%{?with_python3}
%{py3_build}
%endif


%install
%{py2_install}
%if 0%{?with_python3}
%{py3_install}
%endif

# don't package the benchmark test
rm -f %{buildroot}/%{_bindir}/falcon-bench


%check
nosetests-%{python2_version}
%if 0%{?with_python3}
nosetests-%{python3_version}
%endif


%files -n python2-falcon
%doc README.rst
%{python2_sitearch}/falcon*

%if 0%{?with_python3}
%files -n python3-falcon
%doc README.rst
%{python3_sitearch}/falcon*
%endif


%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 01 2015 Carl George <carl.george@rackspace.com> - 0.3.0-1
- Upstream 0.3.0
- Add patch1 to fix GH#558
- Update to new packaging guidelines
- Add new test suite dependencies
- Call nosetests directly

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.10-5
- Upstream 0.1.10
- No python3 in EL7

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Jamie Lennox <jamielennox@redhat.com> - 0.1.8-2
- Remove now missing doc files
- Remove installed test files

* Thu Feb 27 2014 Jamie Lennox <jamielennox@redhat.com> - 0.1.8-1
- Bump to 0.1.8

* Mon Sep 23 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Add Python 3 packaging details and patch to fix for Python 3.
- Remove falcon-bench from package.
- Added check section.

* Wed Sep 18 2013 Jamie Lennox <jamielennox@redhat.com> - 0.1.7-1
- Initial package.
