#!/usr/bin/env python3
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
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is to aid in debugging what virtual environment we are in."""

import os
import pprint
import sys


environment = {}
props = [
    'base_exec_prefix',
    'executable',
    'path',
    'prefix',
    'real_prefix',
    'version']

for prop in props:
    if hasattr(sys, prop):
        environment[prop] = getattr(sys, prop)

environment['VIRTUAL_ENV'] = os.environ.get('VIRTUAL_ENV')

pprint.pprint(environment)
