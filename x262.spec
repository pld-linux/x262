%define		rel	5
Summary:	MPEG-2 encoder based on x264
Summary(pl.UTF-8):	Koder MPEG-2 oparty na x264
Name:		x262
Version:	0
%define	snap	20150316
Release:	0.%{snap}.%{rel}
License:	GPL v2+
Group:		Libraries
# git clone git://git.videolan.org/x262.git
Source0:	%{name}.tar.xz
# Source0-md5:	24b9949ae551f5881c44be65a410b0ee
Patch0:		%{name}-lsmash-update.patch
Patch1:		arch-buildflags.patch
Patch2:		x32.patch
Patch3:		ffmpeg3.patch
URL:		https://www.videolan.org/developers/x262.html
# libswscale libavformat libavcodec libavutil
BuildRequires:	ffmpeg-devel >= 0.7.1
BuildRequires:	ffmpegsource-devel >= 2.16
BuildRequires:	gpac-devel >= 0.5.0-3
BuildRequires:	l-smash-devel >= 1.5
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x262 is an MPEG-2 encoder based on the best-in-class features of x264.

%description -l pl.UTF-8
x262 to koder MPEG-2 oparty na najlepszych cechach x264.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%ifarch x32
%patch2 -p1
%endif
%patch3 -p1

%build
%ifarch x32
export X32="yes"
%endif
%configure \
	--extra-cflags="%{rpmcflags}" \
	--extra-ldflags="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# installs as x264
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

install -D x264 $RPM_BUILD_ROOT%{_bindir}/x262

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/{ratecontrol,vui}.txt
%attr(755,root,root) %{_bindir}/x262
