%define upstream_name 	 File-MimeInfo
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Determine file type
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PA/PARDUS/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README Changes
%_bindir/*
%{perl_vendorlib}/File
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.160.0-3
+ Revision: 765246
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.160.0-1
+ Revision: 759480
- version update 0.16

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-5
+ Revision: 667142
- mass rebuild

* Tue Feb 08 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.150.0-4
+ Revision: 636863
- Rebuild to match system perl version

* Fri Oct 09 2009 Michael Scherer <misc@mandriva.org> 0.150.0-3mdv2010.1
+ Revision: 456256
- rebuild
- rebuild for new perl, to fix #53541

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 405983
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.15-3mdv2009.1
+ Revision: 351749
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.15-2mdv2009.0
+ Revision: 223752
- rebuild

* Fri Feb 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 168829
- update to new version 0.15

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Michael Scherer <misc@mandriva.org> 0.14-1mdv2008.0
+ Revision: 46595
- 0.14

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.13-2mdv2008.0
+ Revision: 23409
- rebuild


* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.13-1mdk
- 0.13

* Mon Oct 10 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdk
- new version 
- %%mkrel
- fix directory ownership
- spec cleanup

* Fri Apr 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.11-1mdk
- 0.11

* Tue Aug 31 2004 Michael Scherer <misc@mandrake.org> 0.10-2mdk 
- add missing BuildRequires

* Tue Aug 24 2004 Michael Scherer <misc@mandrake.org> 0.10-1mdk 
- First Mandrakelinux package

