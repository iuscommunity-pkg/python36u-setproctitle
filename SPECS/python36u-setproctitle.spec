%global python python36u
%global srcname setproctitle

Name:           %{python}-%{srcname}
Version:        1.1.10
Release:        2.ius%{?dist}
Summary:        Python module to customize a process title
License:        BSD
URL:            https://github.com/dvarrazzo/py-setproctitle
Source0:        https://files.pythonhosted.org/packages/source/s/setproctitle/setproctitle-%{version}.tar.gz
BuildRequires:  %{python}-devel
BuildRequires:  %{python}-setuptools


%description
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multi-process systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.


%prep
%setup -q -n %{srcname}-%{version}


%build
%{py36_build}


%install
%{py36_install}


%files
%license COPYRIGHT
%doc README.rst
%{python36_sitearch}/%{srcname}*


%changelog
* Mon Apr 24 2017 Carl George <carl.george@rackspace.com> - 1.1.10-2.ius
- Remove test suite
- Properly install COPYRIGHT file

* Sat Apr 22 2017 evitalis <evitalis@users.noreply.github.com> - 1.1.10-1.ius
- Port from Fedora to IUS
- Latest upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.9-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

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

