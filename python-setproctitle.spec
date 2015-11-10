%if 0%{?fedora}
%global with_python3 1
%endif


%global tarname setproctitle

Name:           python-setproctitle
Version:        1.1.9
Release:        2%{?dist}
Summary:        Python module to customize a process title

License:        BSD
URL:            http://pypi.python.org/pypi/%{tarname}
Source0:        http://pypi.python.org/packages/source/s/%{tarname}/%{tarname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-tools


%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.



%if 0%{?with_python3}
%package -n python3-%{tarname}
Summary:        Python module to customize a process title
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose

%description -n python3-%{tarname}
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multi-process systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.
%endif

%prep
%setup -q -n %{tarname}-%{version}
%{?with_python3: cp -a . %{py3dir}}


%build
CFLAGS="%{optflags}" %{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
chmod 0755 %{buildroot}%{python3_sitearch}/setproctitle*.so
%endif

%check
make tests/pyrun2
# FIXME: tests are broken with python3
%if 0%{?with_python3}
pushd %{py3dir}
BUILD_DIR=$(%{__python3} -c "import sys; import platform; \
print('build/lib.linux-{0}-{1}.{2}'.format(platform.machine(), \
sys.version_info[0], sys.version_info[1]))")
# looks like tests are not 2to3'ed by setup.py
2to3 -w --no-diffs tests
gcc `pkg-config --cflags --libs python3` -o tests/pyrun3 tests/pyrun.c
PYTHONPATH=$BUILD_DIR:$PYTHONPATH ROOT_PATH=$(pwd) LANG=en_US.utf8 \
                                  %{__python3} tests/setproctitle_test.py -v || :
popd
%endif


%files
%doc README.rst COPYRIGHT
# For arch-specific packages: sitearch
%{python2_sitearch}/%{tarname}.so
%{python2_sitearch}/%{tarname}*.egg-info


%if 0%{?with_python3}
%files -n python3-%{tarname}
%doc README.rst COPYRIGHT
# For arch-specific packages: sitearch
%{python3_sitearch}/%{tarname}*.so
%{python3_sitearch}/%{tarname}*.egg-info
%endif

%changelog
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Aug 15 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.9-1
- Upstream 1.1.9

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug  4 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.6-1
- upstream 1.1.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-2
- enable tests execution
- spec cleaning

* Sun Jan 29 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-1
- initial packaging

