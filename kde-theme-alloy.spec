
%define		_name	alloy

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.5.1
Release:	1
License:	X11
Group:		Themes
Source0:	http://kde-look.org/content/files/10605-%{_name}-%{version}.tar.bz2
# Source0-md5:	00fce4a927f01097637dc8ab85452e92
Patch0:		%{_name}-c++.patch
URL:		http://www.kde-look.org/content/show.php?content=2306
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	unsermake
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alloy is a java alloy clone. It features rounded, lightweight and
mildly convex widgets. This package contains an alloy color scheme
which combines a yellow look with blue highlight colors. This package
also contains a kwin decoration with solid background and outlines and
transparent, visible buttons.

%description -l pl
Alloy to kopia stylu o tej samej nazwie stosowanego w aplikacjach
napisanych w javie. Oferuje zaokr±glone, lekkie elementy interfejsu o
subtelnej wypuk³o¶ci. Ten pakiet zawiera schemat kolorów ³±cz±cy ¿ó³ty
wygl±d aplikacji z niebieskimi kolorami pod¶wietlonych elementów menu
i tytu³u okna. Ten pakiet zawiera tak¿e dekoracje kwin
charakteryzuj±c± siê sta³ym (zale¿ny od schematu kolorów) kolorem t³a
i brzegów okna oraz prze¼roczystymi widocznymi przyciskami.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Alloy is a java alloy clone. It features rounded, lightweight and
mildly convex widgets.


%description -n kde-style-%{_name} -l pl
Alloy to kopia stylu o tej samej nazwie stosowanego w aplikacjach
napisanych w javie. Oferuje zaokr±glone, lekkie elementy interfejsu o
subtelnej wypuk³o¶ci.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
This package contains an alloy color scheme which combines a yellow
look with blue highlight colors.

%description -n kde-colorscheme-%{_name} -l pl
Ten pakiet zawiera schemat kolorów ³±cz±cy ¿ó³ty wygl±d aplikacji z
niebieskimi kolorami pod¶wietlonych elementów menu i tytu³u okna.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs

%description -n kde-decoration-%{_name}
This package contains a kwin decoration with solid background and
outlines and transparent, visible buttons.

%description -n kde-decoration-%{_name} -l pl
Ten pakiet zawiera dekoracje kwin charakteryzuj±c± siê sta³ym (zale¿ny
od schematu kolorów) kolorem t³a i brzegów okna oraz prze¼roczystymi
widocznymi przyciskami.



%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.dist

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create dirs if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
##%{_libdir}/kde3/kstyle_*.la
##%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
