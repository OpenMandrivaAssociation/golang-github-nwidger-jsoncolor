# Run tests in check section
%bcond_without check

%global goipath         github.com/nwidger/jsoncolor
%global commit          75a6de4340e59be95f0884b9cebdda246e0fdf40

%global common_description %{expand:
Colorized JSON output for Go.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.5%{?dist}
Summary: Colorized JSON output for Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/fatih/color)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git75a6de4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314git75a6de4
- Fix BuildRequires 

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314git75a6de4
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170215git75a6de4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170215git75a6de4
- First package for Fedora

