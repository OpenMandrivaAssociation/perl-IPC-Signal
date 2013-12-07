%define module IPC-Signal

Summary:	IPC::Signal - Utility functions dealing with signals
Name:		perl-%{module}
Version:	1.00
Release:	9
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~rosch/IPC-Signal/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module contains utility functions for dealing with signals.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/IPC/Signal.pm
%{_mandir}/man3/*

