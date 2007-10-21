Summary:	Extension for blocking unwanted ads, banners etc.
Summary(pl.UTF-8):	Rozszerzenie do blokowania niechcianych reklam, bannerów itp.
%define		_realname	adblock_plus
Name:		seamonkey-addon-adblockplus
Version:	0.7.5.3
Release:	1
Epoch:		1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://addons.mozilla.org/en-US/firefox/downloads/file/19510/%{_realname}-%{version}-fx+tb+sm+fl.xpi
# Source0-md5:	90d7fb085d4a8ef6f5f20ddad8b919a0
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

%description -l pl.UTF-8
Czy denerwują Cię te wszystkie reklamy i bannery, których załadowanie
często trwa dłużej niż wczytanie właściwej treści strony? Adblock Plus
pomoże Ci się ich pozbyć. Kliknij prawym przyciskiem myszki na
bannerze i wybierz "Adblock" z menu kontekstowego - banner już więcej
się nie wyświetli. Możesz też otworzyć panel Adblock Plus aby zobaczyć
listę wszystkich elementów strony i zablokować bannery. Możliwe
również jest tworzenie filtrów używających masek lub nawet wyrażeń
regularnych aby umożliwić blokowanie całych serwisów reklamowych.

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
rm -rf locale/pl-PL/contents.rdf
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
