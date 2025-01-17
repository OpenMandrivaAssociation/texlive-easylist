Name:		texlive-easylist
Version:	32661
Release:	2
Summary:	Lists using a single active character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easylist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to create lists of numbered items (as
in Wittgenstein's 'Tractatus') with a single active character
as the only command. A variety of parameters are available to
configure the appearance of the list; lists may be nested
(effectively to unlimited depth).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easylist/easylist.sty
%doc %{_texmfdistdir}/doc/latex/easylist/README
%doc %{_texmfdistdir}/doc/latex/easylist/easylist-doc.pdf
%doc %{_texmfdistdir}/doc/latex/easylist/easylist-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
