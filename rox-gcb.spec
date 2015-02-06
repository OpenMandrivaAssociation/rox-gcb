Name:		rox-gcb
Version:	0.23
Release:	9
Summary:	Clipboard rox-applet
Group:		Graphical desktop/Other
License:	GPL
URL:		ftp://ftp.atmsk.ru/rox/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%_tmppath/%name-%version
BuildRequires:	libgtksourceview-devel
Requires:	rox

%description
Clipboard rox-applet

%define _appsdir %{_libdir}/apps

%prep
%setup -q -n %{name}

%build
export CFLAGS="$RPM_OPT_FLAGS"
./AppRun --compile

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_appsdir}
cp -a ./ $RPM_BUILD_ROOT%{_appsdir}/%{name}
rm -rf %buildroot/%_appsdir/%name/src

%clean 
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc %{_appsdir}/%name/Help
%dir %{_appsdir}/%name
%{_appsdir}/%name/.DirIcon
%{_appsdir}/%name/App*
%{_appsdir}/%name/Linux-*
%{_appsdir}/%name/gcb.png



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.23-8mdv2010.0
+ Revision: 433388
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.23-7mdv2009.0
+ Revision: 242556
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Sep 03 2006 Götz Waschk <waschk@mandriva.org> 0.23-5mdv2007.0
- Rebuild

* Thu Sep 01 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.23-4mdk
- rebuild to remove glitz dep

* Wed Aug 24 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.23-3mdk
- Rebuild

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.23-2mdk
- rebuild

