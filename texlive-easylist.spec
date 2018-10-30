# revision 32661
# category Package
# catalog-ctan /macros/latex/contrib/easylist
# catalog-date 2012-04-14 11:10:53 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-easylist
Version:	1.3
Release:	12
Summary:	Lists using a single active character
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/easylist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
