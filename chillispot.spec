#
# TODO:
# initscript, requires, cleanups, create as webapp?,

Summary:	ChilliSpot - a Wireless LAN Access Point Controller
Summary(pl.UTF-8):	ChilliSpot - kontroler punktu dostępowego (AP) lokalnej sieci bezprzewodowej
Name:		chillispot
Version:	1.1.0
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.chillispot.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	9d2597756af3fa14d7331b4a3651fc9b
#Source1:	chilli.init
URL:		http://www.chillispot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
#Requires(postun): rpm-helper
#Requires(pre): rpm-helper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ChilliSpot is an open source captive portal or wireless LAN access
point controller. It supports web based login which is today's
standard for public HotSpots and it supports Wireless Protected Access
(WPA) which is the standard of the future. Authentication,
Authorization and Accounting (AAA) is handled by your favorite radius
server. Read more on <http://www.chillispot.org/>.

%description -l pl.UTF-8
ChilliSpot to mający otwarte źródła ograniczony portal lub kontroler
punktu dostępowego (Access Point) bezprzewodowej sieci lokalnej.
Obsługuje logowanie oparte na WWW, będące obecnie standardem dla
publicznych HotSpotów, oraz WPA (Wireless Protected Access), będące
standardem przyszłości. Uwierzytelnianie, autoryzacja i rozliczanie
(Authentication, Authorization, Accounting - AAA) są obsługiwane przy
użyciu wybranego serwera radius. Więcej można przeczytać pod
<http://www.chillispot.org/>.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install doc/chilli.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS doc/firewall.iptables doc/freeradius.users doc/hotspotlogin.cgi
#%attr(755,root,root) /etc/rc.d/init.d/chillispot
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_sbindir}/chilli
%{_mandir}/man8/chilli.8*
