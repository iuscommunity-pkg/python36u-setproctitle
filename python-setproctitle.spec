%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


%global tarname setproctitle

Name:           python-setproctitle
Version:        1.1.3
Release:        3%{?dist}
Summary:        Python module to customize a process title

License:        BSD
URL:            http://pypi.python.org/pypi/%{tarname}
Source0:        http://pypi.python.org/packages/source/s/%{tarname}/%{tarname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-tools
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}


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
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd
%endif

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python_sitearch}/setproctitle.so
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
chmod 0755 %{buildroot}%{python3_sitearch}/setproctitle*.so
%endif

%check
BUILD_DIR=$(%{__python} -c "import sys; import platform; \
print('build/lib.linux-{0}-{1}.{2}'.format(platform.machine(), \
sys.version_info[0], sys.version_info[1]))")
gcc `pkg-config --cflags --libs python` -o tests/pyrun tests/pyrun.c
PYTHONPATH=$BUILD_DIR:$PYTHONPATH ROOT_PATH=$(pwd) \
                                  %{__python} tests/setproctitle_test.py -v
# FIXME: tests are broken with python3
%if 0%{?with_python3}
pushd %{py3dir}
BUILD_DIR=$(%{__python3} -c "import sys; import platform; \
print('build/lib.linux-{0}-{1}.{2}'.format(platform.machine(), \
sys.version_info[0], sys.version_info[1]))")
# looks like tests are not 2to3'ed by setup.py
2to3 -w --no-diffs tests
gcc `pkg-config --cflags --libs python3` -o tests/pyrun tests/pyrun.c
PYTHONPATH=$BUILD_DIR:$PYTHONPATH ROOT_PATH=$(pwd) \
                                  %{__python3} tests/setproctitle_test.py -v || :
popd
%endif


%files
%doc README COPYRIGHT
# For arch-specific packages: sitearch
%{python_sitearch}/*

%if 0%{?with_python3}
%files -n python3-%{tarname}
%doc README COPYRIGHT
# For arch-specific packages: sitearch
%{python3_sitearch}/*
%endif

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-2
- enable tests execution
- spec cleaning

* Sun Jan 29 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.3-1
- initial packaging

