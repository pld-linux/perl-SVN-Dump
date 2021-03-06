#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	SVN
%define		pnam	Dump
Summary:	SVN::Dump - A Perl interface to Subversion dumps
Name:		perl-SVN-Dump
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SVN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c7e62a0399e608bdd9b0968829310490
URL:		http://search.cpan.org/dist/SVN-Dump/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An SVN::Dump object represents a Subversion dump.

This module follow the semantics used in the reference document (the
file notes/fs_dumprestore.txt in the Subversion source tree):

The most basic thing you can do with SVN::Dump is simply copy a dump.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SVN/Dump.pm
%{perl_vendorlib}/SVN/Dump
%{_mandir}/man3/SVN::Dump*
%{_examplesdir}/%{name}-%{version}
