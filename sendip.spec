%define ver 3.0
%define name sendip

Summary: A command line tool to allow sending arbitrary IP packets
Name: %name
Version: %ver
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: http://www.earth.li/projectpurple/files/sendip-%ver.tar.gz
URL: http://www.earth.li/projectpurple/progs/sendip.html
Vendor: Project Purple <projectpurple@earth.li>
Packager: Mike Ricketts <mike@earth.li>
BuildRoot: /var/tmp/sendip-root

%description
A command line tool to send arbitrary IP packets. It has a large number of
command line options to specify the content of every header of a NTP, BGP,
RIP, RIPng, TCP, UDP, ICMP, or raw IPv4 or IPv6 packet.  It also allows any 
data to be added to the packet.

%changelog
* Tue Dec  3 2002 Mike Ricketts <mike@earth.li>
- Update to version 2.3
- RIPng fixes
- Compile on archs requiring alignment

* Sat Oct 12 2002 Mike Ricketts <mike@earth.li>
- Update to version 2.2
- See CHANGES for a more complete list (there's even more than last time)

* Sun Feb 24 2002 Calum Selkirk <cselkirk@panix.com>
- changed /usr/share/man to %{_mandir} and added perl to edit Makefile 
  to refect this
- wrapped %discription to tw=78
- rm buildroot before install
- other minor tweeks

* Sat Feb 23 2002  Mike Ricketts <mike@earth.li>
- Update to version 2.1
- See CHANGES for a more complete list (there's a *lot*)

* Fri Nov 23 2001  Juan Antonio Martinez <jantonio@dit.upm.es>
- Made it FHS aware

* Tue Jul 10 2001  Mike Ricketts <mike@earth.li>
- Update to version 2.0
- See CHANGES for a more complete list

* Mon Dec 25 2000  Mike Ricketts <mike@earth.li>
- Updated to version 1.4
- RIP default
- bugfixes
- contrib

* Wed Nov 29 2000  Mike Ricketts <mike@earth.li>
- Updated to version 1.3
- IPv6, TCP options and other enhancements
- Bugfixes
- See CHANGES for more details

* Sun Oct 22 2000  Mike Ricketts <mike@earth.li>
- Updated to version 1.1
- RIP support (Richard Polton)
- Bugfixes

* Sat Jun 08 2000  Mike Ricketts <mike@earth.li>
- Updated to version 1.0

* Mon Apr 10 2000  Mike Ricketts <mike@earth.li>
- Minor specfile changes, merged with main sendip release

* Thu Apr 06 2000  Devlin Upton <devlin.upton@spectria.com>
- First RPM release.

%prep
%setup

%build
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/lib
make PREFIX=/usr MANDIR=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make PREFIX=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc VERSION README CHANGES LICENSE TODO
%doc /usr/share/man/man1/sendip.1*
%attr(755,root,root) /usr/bin/sendip
%attr(755,root,root) /usr/lib/sendip/*.so
%dir /usr/lib/sendip
