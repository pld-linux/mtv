Summary:	MPEG Video+Audio and Video CD Player with GUI
Summary(pl.UTF-8):	Odtwarzacz MPEG Video+Audio i Video CD z GUI
Name:		mtv
Version:	1.2.5
Release:	1
License:	Shareware/Commercial; not distributable
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.mpegtv.com/pub/mpeg/mpegtv/player/x86-unknown-linux-glibc2.1/packages/TGZ/%{name}-%{version}.tar.gz
# NoSource0-md5: 7025d5ed144cf9ad63e6d909a7d9a877
NoSource:	0
URL:		http://www.mpegtv.com/
Requires:	mtvp = %{version}
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MpegTV Player (mtv) is a realtime software MPEG-1 Video+Audio Player
and VCD Player with GUI. It supports full-screen mode (through
plugin), can play from file, pipe, network URL, or Video CD. It's
shareware/evaluation version.

%description -l pl.UTF-8
MpegTV Player (mtv) jest programowym odtwarzaczem dźwięku i obrazu
MPEG-1 oraz Video CD z graficznym interfejsem użytkownika. Obsługuje
tryb pełnoekranowy (poprzez wtyczkę), może odtwarzać z pliku, rurki,
sieci lub Video CD. To jest wersja shareware do wypróbowania.

%package -n mtvp
Summary:	MPEG Video+Audio and Video CD command-line player
Summary(pl.UTF-8):	Odtwarzacz MPEG Video+Audio i Video CD z linii poleceń
License:	Freeware/Commercial; not distributable
Group:		X11/Applications/Multimedia
Requires:	XFree86-libs

%description -n mtvp
MpegTV Player (mtvp) is a realtime software MPEG-1 Video+Audio Player
and VCD command-line Player. It supports full-screen mode (through
plugin), can play from file, pipe, network URL, or Video CD.

%description -n mtvp -l pl.UTF-8
MpegTV Player (mtvp) jest programowym odtwarzaczem dźwięku i obrazu
MPEG-1 oraz Video CD obsługiwanym z linii poleceń. Obsługuje tryb
pełnoekranowy (poprzez wtyczkę), może odtwarzać z pliku, rurki, sieci
lub Video CD.

%package -n mtvp-fullscreen
Summary:	MPEG Video+Audio and Video CD player - fullscreen plugin
Summary(pl.UTF-8):	Odtwarzacz MPEG Video+Audio i Video CD - wtyczka trybu pełnoekranowego
License:	Freeware/Commercial; not distributable
Group:		X11/Applications/Multimedia
Requires:	mtvp = %{version}
Requires:	SDL >= 1.2.0

%description -n mtvp-fullscreen
This package contains MpegTV fullscreen plugin.

%description -n mtvp-fullscreen -l pl.UTF-8
Ten pakiet zawiera wtyczkę do MpegTV pozwalającą na odtwarzanie w
trybie pełnoekranowym.

%prep
%setup -q -n mtv

%build
# fix hardcoded paths and SDL version
# it's required for compatibility, so license can't prohibit that
# (at least in Poland)
# WARNING: patching binaries, so don't change strings length!
sed 's@libSDL-1\.1@libSDL-1.2@' voh_sdl.so > voh_sdl.so.new
mv -f voh_sdl.so.new voh_sdl.so
for f in mtv mtvp ; do
	sed 's@/usr/local/lib/mtvp/voh/@/usr/./././lib/mtvp/voh/@' $f > $f.new
	mv -f $f.new $f
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/mtvp/voh}

install mtv mtvp $RPM_BUILD_ROOT%{_bindir}
install mtv.1 $RPM_BUILD_ROOT%{_mandir}/man1
install voh_sdl.so $RPM_BUILD_ROOT%{_libdir}/mtvp/voh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mtv
%{_mandir}/man1/mtv.1*

%files -n mtvp
%defattr(644,root,root,755)
%doc COPYRIGHT README LICENSE README-Fullscreen release-notes.html
%attr(755,root,root) %{_bindir}/mtvp

%files -n mtvp-fullscreen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mtvp
