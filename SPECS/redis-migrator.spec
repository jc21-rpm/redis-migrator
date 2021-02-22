%define debug_package %{nil}

%global gh_user jc21

Name:           redis-migrator
Version:        1.0.3
Release:        1%{?dist}
Summary:        Takes the keys from one Redis server/db and transfer them to another server/db 
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Redis Migrator will take the keys from one server/db and transfer them to another server/db 

%prep
%setup -qn %{name}-%{version}

%build
go build -v -ldflags="-X main.version=%{version}" -o bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Feb 22 2021 Jamie Curnow <jc@jc21.com> 1.0.3-1
- https://github.com/jc21/redis-migrator/releases/tag/v1.0.3

* Mon Feb 22 2021 Jamie Curnow <jc@jc21.com> 1.0.2-1
- https://github.com/jc21/redis-migrator/releases/tag/v1.0.2

* Mon Feb 22 2021 Jamie Curnow <jc@jc21.com> 1.0.1-1
- https://github.com/jc21/redis-migrator/releases/tag/v1.0.1

* Thu Feb 11 2021 Jamie Curnow <jc@jc21.com> 1.0.0-1
- https://github.com/jc21/redis-migrator/releases/tag/v1.0.0

* Thu Feb 11 2021 Jamie Curnow <jc@jc21.com> 0.0.2-1
- https://github.com/jc21/redis-migrator/releases/tag/v0.0.2

