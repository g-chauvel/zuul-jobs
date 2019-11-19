# Copyright 2019 Red Hat, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import remarshal


def get_location(prefix, location):
    # To support usage with both docker and podman, the buildset
    # registry keeps "docker.io" entries un-namespaced.
    if prefix == 'docker.io':
        return location
    else:
        return location + '/' + prefix


def ansible_main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='path'),
            buildset_registry=dict(type='raw'),
            buildset_registry_alias=dict(type='str'),
            namespaces=dict(type='raw'),
        )
    )
    p = module.params
    location = '%s:%s' % (p['buildset_registry_alias'],
                          p['buildset_registry']['port'])

    if os.path.exists(p['path']):
        with open(p['path'], 'rb') as f:
            input_data = f.read()
        data = remarshal.decode('toml', input_data, True)
    else:
        data = {}

    unseen = set(p['namespaces'])
    if 'registry' not in data:
        data['registry'] = []
    for reg in data['registry']:
        if reg['prefix'] in unseen:
            unseen.remove(reg['prefix'])
        else:
            continue
        mirrors = reg.setdefault('mirror', [])
        mirrors.insert(0, {
            'location': get_location(reg['prefix'], location)})
    for prefix in unseen:
        mirrors = [{'location': get_location(prefix, location)},
                   {'location': prefix}]
        reg = {'prefix': prefix,
               'location': prefix,
               'mirror': mirrors}
        data['registry'].append(reg)

    output_data = remarshal.encode_toml(data, True)
    with open(p['path'], 'wb') as f:
        f.write(output_data.encode('utf8'))

    module.exit_json(changed=True, data=data)


if __name__ == '__main__':
    ansible_main()
