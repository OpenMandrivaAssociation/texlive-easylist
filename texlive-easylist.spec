%global tl_name easylist
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Lists using a single active character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easylist
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easylist.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to create lists of numbered items (as in
Wittgenstein's 'Tractatus') with a single active character as the only
command. A variety of parameters are available to configure the
appearance of the list; lists may be nested (effectively to unlimited
depth).

