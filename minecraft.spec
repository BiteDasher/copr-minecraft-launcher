Name:		minecraft-launcher
Version:	1035
Release:	1
Summary:	Minecraft Java Launcher bootstrap
License:	All rights reserved
Source0:	https://launcher.mojang.com/v1/objects/ce9e6169550628003e22de8086e9fe1186c2285e/%{name}
Source1:	https://raw.githubusercontent.com/BiteDasher/copr-minecraft-launcher/master/%{name}.svg
Source2:	https://raw.githubusercontent.com/BiteDasher/copr-minecraft-launcher/master/%{name}.desktop

Requires:	jre-headless
Requires:	atk
Requires:	dbus-libs
Requires:	libdrm
Requires:	fontconfig
Requires:	gtk3
Requires:	xrandr
Requires:	cairo
Requires:	pango

BuildArch:	x86_64

%description
Bootstrap for Minecraft: Java Edition official launcher

%prep
#

%install
install -D -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/symbolic/apps/%{name}.svg
install -D -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/symbolic/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
