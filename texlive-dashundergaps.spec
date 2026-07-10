%global tl_name dashundergaps
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0h
Release:	%{tl_revision}.1
Summary:	Produce gaps that are underlined, dotted or dashed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dashundergaps
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dashundergaps.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands (\underline, \dotuline and \dashuline)
each of which underlines its argument with one of the styles the package
is capable of. A phantom mode is provided, where the underline (of
whatever form) can serve for a 'fill-in block' for student evaluation
sheets.

