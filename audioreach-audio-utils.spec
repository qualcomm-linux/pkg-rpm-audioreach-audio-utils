%global debug_package %{nil}
%global commit      16d37f2ff604c0c5e21eb535cf7c6c9c58c26caf

Name:           audioreach-audio-utils
Version:        1.0.0
Release:        1%{?dist}
Summary:        AudioReach audio route library
License:        BSD-3-Clause-Clear
URL:            https://github.com/AudioReach/audioreach-audio-utils
Source0:        https://github.com/AudioReach/audioreach-audio-utils/archive/%{commit}/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  expat-devel
BuildRequires:  pkgconfig(tinyalsa)

%description
AudioReach audio route library (libaudioroute) for configuring
audio routing on Qualcomm platforms.

%prep
%autosetup -n %{name}-%{commit}

%build
pushd audio-route
autoreconf -fi
./configure --prefix=%{_prefix} --libdir=%{_libdir} --includedir=%{_includedir} --disable-static
%make_build
popd

%install
pushd audio-route
%make_install
popd
find %{buildroot} -name '*.la' -delete

%files
%license LICENSE
%{_libdir}/libaudioroute.so
%{_libdir}/pkgconfig/audioroute.pc
%{_includedir}/audio_route/

%changelog
* Thu Sep 18 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 1.0.0-1
- Use proper upstream version 1.0.0 instead of git snapshot notation
- Drop shortcommit and commitdate globals; keep commit hash for Source0

* Wed Oct 30 2024 Qualcomm Linux <quic_linux@quicinc.com> - 0^20241030git16d37f2f-1
- Initial RPM packaging of audioreach-audio-utils for AudioReach components
