# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyWheel(Package):
    """Only needed because other mock packages use PythonPackage"""

    homepage = "http://www.example.com"
    url = "http://www.example.com/wheel-1.0.tar.gz"

    version("1.0", "0123456789abcdef0123456789abcdef")
