%define upstream_name 	 File-MimeInfo
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Determine file type

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/P/PA/PARDUS/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::BaseDir) >= 0.30.0
BuildRequires: perl(File::DesktopEntry) >= 0.40.0
BuildRequires: perl(Pod::Usage)
BuildRequires: perl-devel
BuildArch:  noarch
Requires:   perl(File::BaseDir) >= 0.30.0

%description
This module can be used to determine the mime type of a file; it's a 
replacement for File::MMagic trying to implement the freedesktop 
specification for using the shared mime-info database. The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml MYMETA.yml
%{_bindir}/mimeopen
%{_bindir}/mimetype
%{perl_vendorlib}/File
%{_mandir}/*/*

