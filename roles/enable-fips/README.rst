Enable FIPS on a node.

Set a node into FIPS mode, to test functionality when crypto
policies are set to FIPS in RHEL 8/Centos 8.

The role will set the node into FIPS mode, reboot the node, and
then call the post-reboot-tasks role.  This role requires a role
parameter - nslookup_target.
