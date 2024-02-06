# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

%global _lto_cflags %{nil}

Name: python-numpy
Epoch: 100
Version: 2.2.6
Release: 1%{?dist}
Summary: Fundamental package for array computing with Python
License: BSD-3-Clause
URL: https://github.com/numpy/numpy/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9
BuildRequires: flexiblas-devel
%else
BuildRequires: openblas-devel
%endif
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: git
BuildRequires: lapack-devel
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-meson-python
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python-rpm-macros

%description
NumPy is the fundamental package for scientific computing with Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9
    --config-settings=setup-args="-Dblas=flexiblas" \
    --config-settings=setup-args="-Dlapack=flexiblas" \
%endif
    .

%install
export CFLAGS="%{optflags} -fno-strict-aliasing"
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-numpy
Summary: Fundamental package for array computing with Python
Requires: python3
Provides: python3-numpy = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-numpy
NumPy is the fundamental package for scientific computing with Python.

%package -n python%{python3_version_nodots}-numpy-devel
Summary: Development files for numpy applications
Requires: lapack-devel
Requires: openblas-devel
Requires: python3-devel
Requires: python%{python3_version_nodots}-numpy = %{epoch}:%{version}-%{release}
Provides: python3-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy-devel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-numpy-devel
This package contains files for developing applications using numpy.

%files -n python%{python3_version_nodots}-numpy
%license LICENSE.txt
%{_bindir}/*
%{python3_sitearch}/*
%exclude %{python3_sitearch}/numpy/*/include/
%exclude %{python3_sitearch}/numpy/*/lib/libnpymath.a
%exclude %{python3_sitearch}/numpy/*/lib/libnpyrandom.a
%exclude %{python3_sitearch}/numpy/distutils/*/*.c
%exclude %{python3_sitearch}/numpy/f2py/src/

%files -n python%{python3_version_nodots}-numpy-devel
%{python3_sitearch}/numpy/*/include/
%{python3_sitearch}/numpy/*/lib/libnpymath.a
%{python3_sitearch}/numpy/*/lib/libnpyrandom.a
%{python3_sitearch}/numpy/distutils/*/*.c
%{python3_sitearch}/numpy/f2py/src/
%endif

%if 0%{?sle_version} > 150000
%package -n python3-numpy
Summary: Fundamental package for array computing with Python
Requires: python3
Provides: python3-numpy = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy) = %{epoch}:%{version}-%{release}

%description -n python3-numpy
NumPy is the fundamental package for scientific computing with Python.

%package -n python3-numpy-devel
Summary: Development files for numpy applications
Requires: lapack-devel
Requires: openblas-devel
Requires: python3-devel
Requires: python3-numpy = %{epoch}:%{version}-%{release}
Provides: python3-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy-devel) = %{epoch}:%{version}-%{release}

%description -n python3-numpy-devel
This package contains files for developing applications using numpy.

%files -n python3-numpy
%license LICENSE.txt
%{_bindir}/*
%{python3_sitearch}/*
%exclude %{python3_sitearch}/numpy/*/include/
%exclude %{python3_sitearch}/numpy/*/lib/libnpymath.a
%exclude %{python3_sitearch}/numpy/*/lib/libnpyrandom.a
%exclude %{python3_sitearch}/numpy/distutils/*/*.c
%exclude %{python3_sitearch}/numpy/f2py/src/

%files -n python3-numpy-devel
%{python3_sitearch}/numpy/*/include/
%{python3_sitearch}/numpy/*/lib/libnpymath.a
%{python3_sitearch}/numpy/*/lib/libnpyrandom.a
%{python3_sitearch}/numpy/distutils/*/*.c
%{python3_sitearch}/numpy/f2py/src/
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-numpy
Summary: Fundamental package for array computing with Python
Requires: python3
Provides: python3-numpy = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy) = %{epoch}:%{version}-%{release}

%description -n python3-numpy
NumPy is the fundamental package for scientific computing with Python.

%package -n python3-numpy-f2py
Summary: f2py for numpy
Requires: python3-devel
Requires: python3-numpy = %{epoch}:%{version}-%{release}
Provides: f2py = %{epoch}:%{version}-%{release}
Provides: numpy-f2py = %{epoch}:%{version}-%{release}
Provides: python3-f2py = %{epoch}:%{version}-%{release}
Provides: python3-numpy-f2py = %{epoch}:%{version}-%{release}
Provides: python3dist(numpy-f2py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-numpy-f2py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(numpy-f2py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-numpy-f2py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(numpy-f2py) = %{epoch}:%{version}-%{release}

%description -n python3-numpy-f2py
This package includes a version of f2py that works properly with NumPy.

%files -n python3-numpy
%license LICENSE.txt
%{python3_sitearch}/*
%exclude %{python3_sitearch}/numpy/f2py

%files -n python3-numpy-f2py
%{_bindir}/*
%{python3_sitearch}/numpy/f2py
%endif

%changelog
