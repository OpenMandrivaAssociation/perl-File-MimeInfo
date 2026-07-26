%define upstream_name File-MimeInfo
Name:       perl-%{upstream_name}
Version:    0.37
Release:    2

Summary:    Determine file type

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://codeberg.org/michielb/File-MimeInfo
Source0:    https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::BaseDir) >= 0.30.0
BuildRequires: perl(File::DesktopEntry) >= 0.40.0
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(File::BaseDir)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRequires: pkgconfig(shared-mime-info)
BuildArch:  noarch
Requires:   perl(File::BaseDir) >= 0.30.0

%description
This module can be used to determine the mime type of a file; it's a 
replacement for File::MMagic trying to implement the freedesktop 
specification for using the shared mime-info database. The package
comes with a script called 'mimetype' that can be used as a file(1)
work-alike.

%prep
%setup -q -n %{upstream_name}-%{version}
%autopatch -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%make_install

%files
%doc Changes META.json META.yml
%{_bindir}/mimeopen
%{_bindir}/mimetype
%{perl_vendorlib}/File
%{_mandir}/*/*
