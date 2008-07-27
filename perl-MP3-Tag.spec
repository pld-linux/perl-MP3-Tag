# ToDo:
# - include tk-tag/tk-tag.pl or not? Maybe as a seperate package (more R:)?
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MP3
%define		pnam	Tag
#
Summary:	Module for reading/writing tags of MP3 audio files
Summary(pl.UTF-8):	Moduł do odczytywania/zapisywania znaczników z plików MP3
Name:		perl-MP3-Tag
Version:	0.9710
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	743193ea3c608f0b5954dedbf1a7f94a
URL:		http://search.cpan.org/dist/MP3-Tag/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.21-3
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl module to read/write ID3v1, ID3v1.1 and ID3v2.3
tags of MP3 files. (Other tags hopefully to follow).

%description -l pl.UTF-8
Moduł Perla służący do odczytywania/zapisywania znaczników MP3 typu
ID3v1, ID3v1.1 oraz ID3v2.3 (inne znaczniki w przyszłości).

%description -l ru.UTF-8

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
%attr(755,root,root) %{_bindir}/audio_rename
%attr(755,root,root) %{_bindir}/mp3info2
%attr(755,root,root) %{_bindir}/typeset_audio_dir
%{perl_vendorlib}/MP3/*.pm
%{perl_vendorlib}/MP3/Tag
%{_mandir}/man1/*
%{_mandir}/man3/*
