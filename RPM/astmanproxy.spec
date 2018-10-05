# Created by iglov@avalon.land
%define locsbindir /usr/local/sbin

Name:           astmanproxy
Version:        1.0
Release:        1%{?dist}
Summary:        Some proxy asterisk shit

License:        BSD-like
URL:            https://github.com/iglov/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  openssl-devel
Requires:       openssl

%description
The need for a proxy to Asterisk's manager interface has been 
clear; almost all GUIs and other interfaces to asterisk implement a 
proxy of some kind.  Why?  A proxy offers:

 - A single persistent connection to asterisk
 - A more secure (non-root) TCP interface
 - Ability to offer filtered input/output
 - Less connections and networking load for asterisk

It can serve as the basis for an extensible application framework
for communication with multiple Asterisk servers.

%prep
%autosetup -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%define _unpackaged_files_terminate_build 0
%defattr(-, root, root)
%doc README
%{_sharedstatedir}/asterisk/certs/*
%{locsbindir}/*
/usr/lib/%{name}/*
/var/lib/asterisk/*
/etc/asterisk/*

%changelog
* Thu Oct 5 2018  - 1.0-1
- Initial package.
