# revision 22362
# category Package
# catalog-ctan /macros/latex/contrib/easylist
# catalog-date 2010-02-28 15:24:01 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-easylist
Version:	1.3
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package allows you to create lists of numbered items (as
in Wittgenstein's 'Tractatus') with a single active character
as the only command. A variety of parameters are available to
configure the appearance of the list; lists may be nested
(effectively to unlimited depth).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/easylist/easylist.sty
%doc %{_texmfdistdir}/doc/latex/easylist/README
%doc %{_texmfdistdir}/doc/latex/easylist/easylist-doc.pdf
%doc %{_texmfdistdir}/doc/latex/easylist/easylist-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
