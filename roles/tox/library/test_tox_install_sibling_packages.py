# Copyright (C) 2019 VEXXHOST, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import sys
import testtools

from .tox_install_sibling_packages import get_installed_packages


class TestToxInstallSiblingPackages(testtools.TestCase):
    def test_get_installed_packages(self):
        # NOTE(mnaser): Given that we run our tests inside Tox, we can
        #               leverage the tox virtual environment we use in
        #               unit tests instead of mocking up everything.
        pkgs = get_installed_packages(sys.executable)

        # NOTE(mnaser): Zuul should be installed in this virtualenv
        #               but this might fail later if we stop adding Zuul
        #               in the unit tests.
        self.assertIn("zuul", pkgs)
