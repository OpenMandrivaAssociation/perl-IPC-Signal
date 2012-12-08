%define module IPC-Signal

Summary:	IPC::Signal - Utility functions dealing with signals
Name:		perl-%{module}
Version:	1.00
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~rosch/IPC-Signal/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module contains utility functions for dealing with signals.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/IPC/Signal.pm
%{_mandir}/*/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.00-5mdv2010.0
+ Revision: 430476
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.00-4mdv2009.0
+ Revision: 257387
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.00-3mdv2009.0
+ Revision: 245410
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.00-1mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdv2007.0
+ Revision: 131200
- Import perl-IPC-Signal

* Wed Feb 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

