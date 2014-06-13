# revision 23373
# category Package
# catalog-ctan /macros/latex/contrib/dashundergaps
# catalog-date 2010-01-23 00:15:17 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-dashundergaps
Version:	1.2
Release:	7
Summary:	Underline with dotted or dashed lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashundergaps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands (\underline, \dotuline and
\dashuline) each of which underlines its argument with one of
the styles the package is capable of. A phantom mode is
provided, where the underline (of whatever form) can serve for
a 'fill-in block' for student evaluation sheets.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dashundergaps/dashundergaps.sty
%doc %{_texmfdistdir}/doc/latex/dashundergaps/README
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/pdf/dashundergaps.pdf
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/tex/Makefile
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/tex/dashundergaps-bib.bib
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/tex/dashundergaps.forlisting
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/tex/dashundergaps.tex
%doc %{_texmfdistdir}/doc/latex/dashundergaps/doc/tex/perso.ist

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 750766
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718202
- texlive-dashundergaps
- texlive-dashundergaps
- texlive-dashundergaps
- texlive-dashundergaps

