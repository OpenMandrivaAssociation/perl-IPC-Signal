%define module IPC-Signal

Summary:	IPC::Signal - Utility functions dealing with signals
Name:		perl-%{module}
Version:	1.00
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~rosch/IPC-Signal/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module contains utility functions for dealing with signals.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor


%make
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std


%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/IPC/Signal.pm
%{_mandir}/*/*


