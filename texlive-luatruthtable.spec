Name:		texlive-luatruthtable
Version:	68893
Release:	1
Summary:	Generate truth tables of boolean values in LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luatruthtable
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatruthtable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatruthtable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an easy way for generating truth tables
of boolean values in LuaLaTeX. The time required for operations
is no issue while compiling with LuaLaTeX. The package supports
nesting of commands for multiple operations. It can be modified
or extended by writing custom lua programs. There is no need to
install lua on users system as TeX distributions (TeX Live or
MikTeX) come bundled with LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luatruthtable
%doc %{_texmfdistdir}/doc/lualatex/luatruthtable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
