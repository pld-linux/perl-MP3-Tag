# ToDo:
# - include tk-tag/tk-tag.pl or not? Maybe as a seperate package (more R:)?
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MP3
%define	pnam	Tag
#
Summary:	Module for reading/writing tags of MP3 audio files
Summary(pl):	Modu³ do odczytywaniu/zapisywania znaczników z plików MP3
Name:		perl-%{pdir}-%{pnam}
Version:	0.92
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3b506afc143cd4cd325666c7f7c4b6e
URL:		http://www.cpan.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl module to read/write ID3v1, ID3v1.1 and ID3v2.3
tags of mp3-files. (Other tags hopefully to follow).

%description -l pl
Modu³ Perla s³u¿±cy do odczytywania/zapisywania znaczników MP3 typu
ID3v1, ID3v1.1 oraz ID3v2.3 (inne znaczniki w przysz³o¶ci).

%description -l ru

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.txt examples/ 
%{perl_vendorlib}/MP3/Tag.pm
%{perl_vendorlib}/MP3/Tag
%{_mandir}/man3/*
