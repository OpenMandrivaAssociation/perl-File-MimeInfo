%define module 	File-MimeInfo
%define name 	perl-%{module}
%define version 0.14
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Determine file type
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PARDUS/%{module}/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-File-BaseDir
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module can be used to determine the mime type of a file; it's a 
replacement for File::MMagic trying to implement the freedesktop 
specification for using the shared mime-info database. The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%_bindir/*
%{perl_vendorlib}/File
%{_mandir}/*/*

