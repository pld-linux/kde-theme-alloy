
%define		_name	alloy

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.5.3
Release:	2
License:	X11
Group:		Themes
Source0:	http://www.kde-look.org/content/files/10605-%{_name}-%{version}.tar.bz2
# Source0-md5:	4c84f744ba0eeda89436e1c671e18c85
Patch0:		%{_name}-c++.patch
URL:		http://www.kde-look.org/content/show.php?content=10605
BuildRequires:	kdebase-devel >= 9:3.2.0
Requires:	kde-decoration-%{_name}
Requires:	kde-style-%{_name}
Requires:	kde-colorscheme-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alloy is a java alloy clone. It features rounded, lightweight and
mildly convex widgets. This package contains an alloy color scheme
which combines a yellow look with blue highlight colors. This package
also contains a kwin decoration with solid background and outlines and
transparent, visible buttons.

%description -l pl.UTF-8
Alloy to kopia stylu o tej samej nazwie stosowanego w aplikacjach
napisanych w Javie. Oferuje zaokrąglone, lekkie elementy interfejsu o
subtelnej wypukłości. Ten pakiet zawiera schemat kolorów łączący żółty
wygląd aplikacji z niebieskimi kolorami podświetlonych elementów menu
i tytułu okna. Ten pakiet zawiera także dekoracje kwin
charakteryzującą się stałym (zależny od schematu kolorów) kolorem tła
i brzegów okna oraz przezroczystymi widocznymi przyciskami.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Alloy is a java alloy clone. It features rounded, lightweight and
mildly convex widgets.

%description -n kde-style-%{_name} -l pl.UTF-8
Alloy to kopia stylu o tej samej nazwie stosowanego w aplikacjach
napisanych w Javie. Oferuje zaokrąglone, lekkie elementy interfejsu o
subtelnej wypukłości.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
This package contains an alloy color scheme which combines a yellow
look with blue highlight colors.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Ten pakiet zawiera schemat kolorów łączący żółty wygląd aplikacji z
niebieskimi kolorami podświetlonych elementów menu i tytułu okna.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl.UTF-8):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop

%description -n kde-decoration-%{_name}
This package contains a kwin decoration with solid background and
outlines and transparent, visible buttons.

%description -n kde-decoration-%{_name} -l pl.UTF-8
Ten pakiet zawiera dekoracje kwin charakteryzującą się stałym (zależny
od schematu kolorów) kolorem tła i brzegów okna oraz przezroczystymi
widocznymi przyciskami.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}" \
	kde_libs_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
