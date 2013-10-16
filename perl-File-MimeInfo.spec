%define modname	File-MimeInfo
%define modver	0.16

Summary:	Determine file type
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PARDUS/%{modname}/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl(Module::Build)

%description
This module can be used to determine the mime type of a file; it's a 
replacement for File::MMagic trying to implement the freedesktop 
specification for using the shared mime-info database. The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/*
%{perl_vendorlib}/File
%{_mandir}/man1/*
%{_mandir}/man3/*

