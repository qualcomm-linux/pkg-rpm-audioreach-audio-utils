%global debug_package %{nil}

Name:           audioreach-audio-utils
Version:        1.0.1
Release:        1%{?dist}
Summary:        AudioReach audio route library
License:        BSD-3-Clause-Clear
URL:            https://github.com/AudioReach/audioreach-audio-utils
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers, the unversioned shared-object symlink, and the
pkg-config file for building against libaudioroute.

%prep
%autosetup -n %{name}-%{version}

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
%{_libdir}/libaudioroute.so.*

%files devel
%{_includedir}/audio_route/
%{_libdir}/libaudioroute.so
%{_libdir}/pkgconfig/audioroute.pc

%changelog
* Fri Sep 25 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 1.0.1-1
- Build from the upstream v1.0.1 release tag instead of a pre-1.0.0
  commit so the packaged version matches the sources
- Package the versioned libaudioroute.so.* soname introduced in v1.0.1
- Split development files (headers, unversioned .so, pkg-config) into
  a -devel subpackage, matching the shared-library layout used by the
  other AudioReach packages

* Thu Sep 18 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 1.0.0-1
- Use proper upstream version 1.0.0 instead of git snapshot notation
- Drop shortcommit and commitdate globals; keep commit hash for Source0

* Wed Oct 30 2024 Qualcomm Linux <quic_linux@quicinc.com> - 0^20241030git16d37f2f-1
- Initial RPM packaging of audioreach-audio-utils for AudioReach components
