Name:		texlive-dashundergaps
Version:	58150
Release:	2
Summary:	Underline with dotted or dashed lines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dashundergaps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/dashundergaps
%doc %{_texmfdistdir}/doc/latex/dashundergaps

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
