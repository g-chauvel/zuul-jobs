#!/usr/bin/env python
#
# Copyright 2019 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Update job definitions for multi-platform jobs, and make sure every
# in-repo test job appears in a project definition.  This script
# re-writes the files in zuul-tests.d.  It should be run from the root
# of the repo.

import os

from ruamel.yaml.comments import CommentedMap

import ruamellib

# There are fedora- and debian-latest nodesets, but they can't be used
# in the multinode jobs, so just use the real labels everywhere.

PLATFORMS = [
    'centos-7',
    'debian-stretch',
    'fedora-29',
    'opensuse-15',
    'opensuse-tumbleweed',
    'ubuntu-bionic',
    'ubuntu-trusty',
    'ubuntu-xenial',
]


def get_nodeset(platform, multinode):
    d = CommentedMap()
    if not multinode:
        d['nodes'] = [
            CommentedMap([('name', platform), ('label', platform)]),
        ]
    else:
        d['nodes'] = [
            CommentedMap([('name', 'primary'), ('label', platform)]),
            CommentedMap([('name', 'secondary'), ('label', platform)]),
        ]
        d['groups'] = [
            CommentedMap([('name', 'switch'), ('nodes', ['primary'])]),
            CommentedMap([('name', 'peers'), ('nodes', ['secondary'])]),
        ]
    return d


def handle_file(fn):
    yaml = ruamellib.YAML()
    data = yaml.load(open(fn))
    outdata = []
    outprojects = []
    joblist = []
    for obj in data:
        if 'job' in obj:
            job = obj['job']
            if 'auto-generated' in job.get('tags', []):
                continue
            outdata.append(obj)
            tags = job.get('tags', [])
            all_platforms = False
            if 'all-platforms-multinode' in tags:
                multinode = True
                all_platforms = True
            elif 'all-platforms' in tags:
                all_platforms = True
                multinode = False
            if all_platforms:
                for platform in PLATFORMS:
                    ojob = CommentedMap()
                    ojob['name'] = job['name'] + '-' + platform
                    desc = job['description'].split('\n')[0]
                    ojob['description'] = desc + ' on ' \
                        + platform
                    ojob['parent'] = job['name']
                    ojob['tags'] = 'auto-generated'
                    ojob['nodeset'] = get_nodeset(platform, multinode)
                    outdata.append({'job': ojob})
                    joblist.append(ojob['name'])
            else:
                joblist.append(job['name'])
        elif 'project' in obj:
            outprojects.append(obj)
        else:
            outdata.append(obj)
    # We control the last project stanza
    outdata.extend(outprojects)
    project = outprojects[-1]['project']
    project['check']['jobs'] = joblist
    project['gate']['jobs'] = joblist
    with open(fn, 'w') as f:
        yaml.dump(outdata, stream=f)


def main():
    for f in os.listdir('zuul-tests.d'):
        if not f.endswith('.yaml'):
            continue
        if f == 'project.yaml':
            continue
        handle_file(os.path.join('zuul-tests.d', f))


if __name__ == "__main__":
    main()
