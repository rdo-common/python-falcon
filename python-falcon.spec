# F26 is the first version with pytest > 3
%if 0%{?fedora} >= 26
%bcond_without tests
%else
%bcond_with tests
%endif

%global srcname falcon

Name:           python-%{srcname}
Version:        1.4.0
Release:        1%{?dist}
Summary:        An unladen web framework for building APIs and app backends
License:        ASL 2.0
URL:            https://falconframework.org
Source0:        https://files.pythonhosted.org/packages/source/%(cut -c1 <<< %{srcname})/%{srcname}/%{srcname}-%{version}.tar.gz
Patch005:       005-versioned-console-scripts.patch


%description
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%package -n python2-%{srcname}
Summary:        %{summary}
# build
BuildRequires:  python2-devel
BuildRequires:  python%{?fedora:2}-setuptools
BuildRequires:  %{?fedora:python2-}Cython
%if %{with tests}
# tests
BuildRequires:  %{?fedora:python2-}pytest >= 3.0.1
BuildRequires:  python%{?fedora:2}-yaml
BuildRequires:  python%{?fedora:2}-requests
BuildRequires:  python%{?fedora:2}-six >= 1.4.0
BuildRequires:  python%{?feodra:2}-testtools
BuildRequires:  python2-msgpack
BuildRequires:  python2-jsonschema
%endif
# runtime
Requires:       python%{?fedora:2}-six >= 1.4.0
Requires:       python2-mimeparse >= 1.5.2
%{?fedora:Recommends: python2-ujson}
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
# build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython
%if %{with tests}
# tests
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.0.1
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-six >= 1.4.0
BuildRequires:  python%{python3_pkgversion}-testtools
BuildRequires:  python%{python3_pkgversion}-msgpack
BuildRequires:  python%{python3_pkgversion}-jsonschema
%endif
# runtime
Requires:       python%{python3_pkgversion}-six >= 1.4.0
Requires:       python%{python3_pkgversion}-mimeparse >= 1.5.2
%{?fedora:Recommends: python3-ujson}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
Falcon is a high-performance Python framework for building cloud APIs.
It encourages the REST architectural style, and tries to do as little as
possible while remaining highly effective.


%prep
%autosetup -p 1 -n %{srcname}-%{version}


%build
%py2_build
%py3_build


%install
%py3_install
%py2_install


%if %{with tests}
%check
pytest-%{python2_version} tests
pytest-%{python3_version} tests
%endif


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/falcon*
%{_bindir}/falcon-bench
%{_bindir}/falcon-bench-2
%{_bindir}/falcon-bench-%{python2_version}
%{_bindir}/falcon-print-routes
%{_bindir}/falcon-print-routes-2
%{_bindir}/falcon-print-routes-%{python2_version}


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/falcon*
%{_bindir}/falcon-bench-3
%{_bindir}/falcon-bench-%{python3_version}
%{_bindir}/falcon-print-routes-3
%{_bindir}/falcon-print-routes-%{python3_version}


%changelog
* Tue Jan 16 2018 Carl George <carl@george.computer> - 1.4.0-1
- Latest upstream rhbz#1528076
- Recommend ujson on Fedora

* Thu Sep 07 2017 Carl George <carl@george.computer> - 1.3.0-1
- Latest upstream
- Enable python34 EPEL subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Carl George <carl.george@rackspace.com> - 1.2.0-4
- The test test_deprecated_decorator fails in Koji, add patch006 to skip

* Fri Jun 09 2017 Carl George <carl.george@rackspace.com> - 1.2.0-3
- Only run test suite on F26+ due to pytest 3 requirement

* Thu May 04 2017 Carl George <carl.george@rackspace.com> - 1.2.0-2
- Spec file clean up
- Fix rpmlint error caused by srcname being undefined

* Tue May 02 2017 Carl George <carl.george@rackspace.com> - 1.2.0-1
- Latest upstream
- Switch from nosetests to pytest
- Require mimeparse >= 1.5.2 (related rhbz#1339379)
- Add Patch005 to create versioned scripts
- Include LICENSE

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
