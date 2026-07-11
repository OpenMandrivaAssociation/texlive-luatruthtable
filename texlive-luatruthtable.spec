%global tl_name luatruthtable
%global tl_revision 78415

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Generate truth tables of boolean values in LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luatruthtable
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatruthtable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatruthtable.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an easy way for generating truth tables of boolean
values in LuaLaTeX. The time required for operations is no issue while
compiling with LuaLaTeX. The package supports nesting of commands for
multiple operations. It can be modified or extended by writing custom
Lua programs. There is no need to install Lua on users system as TeX
distributions (TeX Live or MiKTeX) come bundled with LuaLaTeX.

