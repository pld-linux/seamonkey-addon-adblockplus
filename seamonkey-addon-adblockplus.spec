Summary:	Extension for blocking unwanted ads, banners etc.
Summary(pl):	Rozszerzenie do blokowania niechcianych reklam, bannerów itp.
%define		_realname	adblock_plus
Name:		seamonkey-addon-adblockplus
Version:	0.7.2.4
Release:	1
Epoch:		1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/mozilla.org/extensions/%{_realname}/%{_realname}-%{version}-fx+fl+zm+tb.xpi
# Source0-md5:	bb01339af68b393f8039e4ad0f813a5e
Source1:	adblockplus-installed-chrome.txt
URL:		http://adblockplus.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	seamonkey >= 1.0
Requires:	seamonkey >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ever been annoyed by all those ads and banners on the internet that
often take longer to download than everything else on the page?
Adblock Plus will help you to get rid of them. Right-click on a banner
and choose "Adblock" from the context menu - the banner won't be
downloaded again. Or open Adblock Plus sidebar to see all elements of
the page and block the banners. You can use filters with wildcards or
even regular expressions to block complete banner factories.

%description -l pl
Czy denerwuj± Ciê te wszystkie reklamy i bannery, których za³adowanie
czêsto trwa d³u¿ej ni¿ wczytanie w³a¶ciwej tre¶ci strony? Adblock Plus
pomo¿e Ci siê ich pozbyæ. Kliknij prawym przyciskiem myszki na
bannerze i wybierz "Adblock" z menu kontekstowego - banner ju¿ wiêcej
siê nie wy¶wietli. Mo¿esz te¿ otworzyæ panel Adblock Plus aby zobaczyæ
listê wszystkich elementów strony i zablokowaæ bannery. Mo¿liwe
równie¿ jest tworzenie filtrów u¿ywaj±cych masek lub nawet wyra¿eñ
regularnych aby umo¿liwiæ blokowanie ca³ych serwisów reklamowych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/seamonkey
install -d $RPM_BUILD_ROOT%{_libdir}/seamonkey

unzip %{SOURCE0} -d $RPM_BUILD_ROOT

# fix polish locale
PWD=`pwd`
cd $RPM_BUILD_ROOT/chrome/
unzip adblockplus.jar locale/pl-PL/contents.rdf
sed -i -e 's/locale:pl/locale:pl-PL/g' locale/pl-PL/contents.rdf
zip -0 adblockplus.jar locale/pl-PL/contents.rdf
cd $PWD

install %{SOURCE1} $RPM_BUILD_ROOT/chrome
mv $RPM_BUILD_ROOT/defaults/preferences $RPM_BUILD_ROOT/defaults/pref
mv $RPM_BUILD_ROOT/{chrome,defaults} $RPM_BUILD_ROOT%{_datadir}/seamonkey
mv $RPM_BUILD_ROOT/components $RPM_BUILD_ROOT%{_libdir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_datadir}/seamonkey/chrome/adblockplus.jar
%{_datadir}/seamonkey/chrome/adblockplus-installed-chrome.txt
%{_datadir}/seamonkey/defaults/pref/adblockplus.js
%{_libdir}/seamonkey/components/nsAdblockPlus.*
