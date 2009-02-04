Name:           ocaml-pgocaml
Version:        1.1
Release:        %mkrel 2
Summary:        OCaml library for type-safe access to PostgreSQL databases

Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://developer.berlios.de/projects/pgocaml/
Source0:        http://download.berlios.de/pgocaml/pgocaml-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  postgresql-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-extlib-devel
BuildRequires:  pcre-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-calendar-devel >= 2.0.4
BuildRequires:  ocaml-csv-devel
BuildRequires:  camlp4

Requires:  ocaml-pcre
Requires:  ocaml-extlib
Requires:  ocaml-calendar

%description
PG'OCaml is a type-safe, simple interface to PostgreSQL from OCaml.
It lets you embed SQL statements directly into OCaml code.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pgocaml-%{version}


%build
# Don't build or run the test programs because that would need
# a live PostgreSQL database around.
make pGOCaml_config.ml pgocaml.cma pgocaml.cmxa pa_pgsql.cmo \
  pgocaml_prof META
make doc
strip pgocaml_prof


%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocamlfind install pgocaml META *.mli *.cmi *.cmx *.cma *.cmxa *.a pa_*.cmo

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 pgocaml_prof %{buildroot}%{_bindir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%{_libdir}/ocaml/pgocaml
%exclude %{_libdir}/ocaml/pgocaml/*.a
%exclude %{_libdir}/ocaml/pgocaml/*.cmxa
%exclude %{_libdir}/ocaml/pgocaml/*.cmx
%exclude %{_libdir}/ocaml/pgocaml/*.mli
%{_bindir}/pgocaml_prof


%files devel
%defattr(-,root,root,-)
%doc README.txt README.profiling BUGS.txt CONTRIBUTORS.txt COPYING.LIB HOW_IT_WORKS.txt html/*
%{_libdir}/ocaml/pgocaml/*.a
%{_libdir}/ocaml/pgocaml/*.cmxa
%{_libdir}/ocaml/pgocaml/*.cmx
%{_libdir}/ocaml/pgocaml/*.mli
