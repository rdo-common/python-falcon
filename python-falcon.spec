# what it's called on pypi
%global srcname falcon
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Falcon is a high-performance Python framework for building cloud APIs.  It
encourages the REST architectural style, and tries to do as little as possible
while remaining highly effective.}

# F26 is the first version with pytest > 3
%if 0%{?fedora} >= 26
%bcond_without  tests
%else
%bcond_with     tests
%endif

%bcond_without  python3

%if (%{defined fedora} && 0%{?fedora} < 31) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

Name:           python-%{pkgname}
Version:        1.4.1
Release:        7%{?dist}
Summary:        An unladen web framework for building APIs and app backends
License:        ASL 2.0
URL:            https://falconframework.org
Source0:        %pypi_source
Patch005:       005-versioned-console-scripts.patch
BuildRequires:  gcc


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
# build
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-Cython
%if %{with tests}
# tests
BuildRequires:  python2-pytest >= 3.0.1
BuildRequires:  python%{?fedora:2}-yaml
BuildRequires:  python2-requests
BuildRequires:  python2-six >= 1.4.0
BuildRequires:  python%{?fedora:2}-testtools
BuildRequires:  python2-msgpack
BuildRequires:  python2-jsonschema
%endif
# runtime
Requires:       python2-six >= 1.4.0
Requires:       python2-mimeparse >= 1.5.2
%{?fedora:Recommends: python2-ujson}
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
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
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}
%endif


%prep
%autosetup -p 1 -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}


%install
%{?with_python3:%py3_install}
%{?with_python2:%py2_install}


%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitearch} pytest-%{python2_version} tests}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitearch} pytest-%{python3_version} tests}
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{libname}
%{python2_sitearch}/%{eggname}-%{version}-py%{python2_version}.egg-info
%{_bindir}/falcon-bench
%{_bindir}/falcon-bench-2
%{_bindir}/falcon-bench-%{python2_version}
%{_bindir}/falcon-print-routes
%{_bindir}/falcon-print-routes-2
%{_bindir}/falcon-print-routes-%{python2_version}
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{libname}
%{python3_sitearch}/%{eggname}-%{version}-py%{python3_version}.egg-info
%{!?with_python2:%{_bindir}/falcon-bench}
%{_bindir}/falcon-bench-3
%{_bindir}/falcon-bench-%{python3_version}
%{!?with_python2:%{_bindir}/falcon-print-routes}
%{_bindir}/falcon-print-routes-3
%{_bindir}/falcon-print-routes-%{python3_version}
%endif


%changelog
* Mon Apr 22 2019 Carl George <carl@george.computer> - 1.4.1-7
- Disable python2 subpackage on Fedora 31+ rhbz#1701670
- Run tests from buildroot, not builddir

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-4
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Carl George <carl@george.computer> - 1.4.1-3
- Add BuildRequires for gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Carl George <carl@george.computer> - 1.4.1-1
- Latest upstream rhbz#1535255

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
