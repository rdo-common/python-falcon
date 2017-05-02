%if 0%{?fedora}
%bcond_without python3
%global _docdir_fmt %{name}
%endif

Name:           python-falcon
Version:        1.2.0
Release:        1%{?dist}
Summary:        An unladen web framework for building APIs and app backends
License:        ASL 2.0
URL:            https://falconframework.org
Source0:        https://files.pythonhosted.org/packages/source/f/falcon/falcon-%{version}.tar.gz

Patch001:       001-disable_coverage.patch

# The mimeparse module [1] appears to be abandonded, but is still what is
# packaged in Fedora.  The python-mimeparse module [2] appears to be actively
# maintained (as of 2016-05-24).  The falcon test suite changed [3] to
# accommodate a bug fix in the newer python-mimeparse module, but that
# inadvertently causes the test suite to fail when using the older mimeparse
# module.  Until we can sort out the mimeparse confusion in Fedora [4], lets
# just revert that change.
#
# [1]: https://code.google.com/archive/p/mimeparse/
# [2]: https://github.com/dbtsai/python-mimeparse
# [3]: https://github.com/falconry/falcon/commit/710a8dd
# [4]: https://bugzilla.redhat.com/show_bug.cgi?id=1339379
#
Patch004:       004-old_mimeparse.patch


%description
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%package -n python2-falcon
Summary:        %{summary}
# build
BuildRequires:  python2-devel
BuildRequires:  python%{?fedora:2}-setuptools
BuildRequires:  %{?fedora:python2-}Cython
# tests
BuildRequires:  python2-ddt
BuildRequires:  python2-mimeparse
BuildRequires:  python%{?fedora:2}-nose
BuildRequires:  python%{?fedora:2}-requests
BuildRequires:  python%{?fedora:2}-six >= 1.4.0
BuildRequires:  python%{?feodra:2}-testtools
BuildRequires:  python%{?fedora:2}-yaml
# runtime
Requires:       python%{?fedora:2}-mimeparse
Requires:       python%{?fedora:2}-six >= 1.4.0
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-falcon
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%if %{with python3}
%package -n python3-falcon
Summary:        %{summary}
# build
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
# tests
BuildRequires:  python3-ddt
BuildRequires:  python3-mimeparse
BuildRequires:  python3-nose
BuildRequires:  python3-requests
BuildRequires:  python3-six >= 1.4.0
BuildRequires:  python3-testtools
BuildRequires:  python3-yaml
# runtime
Requires:       python3-mimeparse
Requires:       python3-six >= 1.4.0
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-falcon
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.
%endif


%prep
%autosetup -p 1 -n falcon-%{version}


%build
%{py2_build}
%if %{with python3}
%{py3_build}
%endif


%install
%{py2_install}
%if %{with python3}
%{py3_install}
%endif

# don't package the benchmark test
rm -f %{buildroot}/%{_bindir}/falcon-bench


%check
nosetests-%{python2_version}
%if %{with python3}
nosetests-%{python3_version}
%endif


%files -n python2-falcon
%doc README.rst
%{python2_sitearch}/falcon*


%if %{with python3}
%files -n python3-falcon
%doc README.rst
%{python3_sitearch}/falcon*
%endif


%changelog
* Tue May 02 2017 Carl George <carl.george@rackspace.com> - 1.2.0-1
- Latest upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 24 2016 Carl George <carl.george@rackspace.com> - 1.0.0-1
- Latest upstream
- Patch002 and Patch003 fixed upstream
- Patch004 added to make test suite pass with old version of mimeparse

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Carl George <carl.george@rackspace.com> - 0.3.0-4
- Specify minimum version of python-six
- Change python3 control macros to a bcond macro
- Add bcond macro to optionally require explicit python2 names

* Mon Nov 16 2015 Carl George <carl.george@rackspace.com> - 0.3.0-3
- Add patch to disable coverage
- Add patch to skip test_request_cookie_parsing on Python 3.5

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
