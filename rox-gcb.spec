Name:		rox-gcb
Version:	0.23
Release:	%mkrel 5
Summary:	Clipboard rox-applet
Group:		Graphical desktop/Other
License:	GPL
URL:		ftp://ftp.atmsk.ru/rox/
Source0:	%{name}-%{version}.tar.gz
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

