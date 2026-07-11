%global tl_name limecv
%global tl_revision 75301

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.12
Release:	%{tl_revision}.1
Summary:	A (Xe/Lua)LaTeX document class for curriculum vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/limecv
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/limecv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/limecv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/limecv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
limecv is a (Xe/Lua)LaTeX document class to write curriculum vitae. It
is designed with the following design rules: simple, elegant and clean.
To this end, it offers several environments and macros for convenience.

