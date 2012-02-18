%bcond_without bootstrap
%global packname  inline
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.3.8
Release:          1
Summary:          Inline C, C++, Fortran function calls from R
Group:            Sciences/Mathematics
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods 
%if %{without bootstrap}
Requires:         R-Rcpp 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
%if %{without bootstrap}
BuildRequires:    R-Rcpp 
%endif

%description
Functionality to dynamically define R functions and S4 methods with
in-lined C, C++ or Fortran code supporting .C and .Call calling

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help