Mirror Configuration
====================

.. note:: This is a work in progress, the zuul-jobs required changes are not implemented yet.

Many roles in `zuul-jobs` can be made aware of local mirrors of
Internet services.  If site mirrors are present, they expect to find a
variable named ``mirror_info``, or ``zuul_site_mirror_info`` if that
is not defined.  This variable is a dictionary which holds keys for
each type of mirror that one or more roles in `zuul-jobs` can work
with.

.. note:: The following example defines a local variable
          ``zuul_site_local_mirror_host`` for convenience, but it is
          not part of the API -- it is only used in defining the
          mirror info dictionary.

For example:

.. code-block:: yaml

   zuul_site_local_mirror_host: "mirror.{{ nodepool.region | lower }}.{{ nodepool.cloud | lower }}.example.org"

   zuul_site_mirror_info:
     pypi:
       url: https://{{ zuul_site_local_mirror_host }}/pypi/simple
     wheel:
       url: https://{{ zuul_site_local_mirror_host }}/wheel
     fedora:
       url: https://{{ zuul_site_local_mirror_host }}/fedora
     opensuse:
       url: https://{{ zuul_site_local_mirror_host }}/opensuse
     debian:
       - url: https://{{ zuul_site_local_mirror_host }}/debian
         components: ['main']
       - url: https://{{ zuul_site_local_mirror_host }}/debian-security
         components: ['main']
     ubuntu:
       - url: https://{{ zuul_site_local_mirror_host }}/ubuntu
         components: ['main', 'universe']
         trusted: true
       - url: https://{{ zuul_site_local_mirror_host }}/ubuntu-security
         components: ['main', 'universe']
         trusted: true
     dockerhub:
       url: https://{{ zuul_site_local_mirror_host }}:8082/


.. zuul:rolevar:: mirror_info

   A dictionary which contains information about the various mirrors
   available.  Each type of mirror is a key in this dictionary; if it
   is not present, then the site does not have that mirror.

   .. zuul:rolevar:: pypi

      .. zuul:rolevar:: url

         The URL for a PyPI mirror.

   .. zuul:rolevar:: wheel

      .. zuul:rolevar:: url

         The URL for a Python wheel mirror.

   .. zuul:rolevar:: fedora

      .. zuul:rolevar:: url

         The URL for a Fedora mirror.

   .. zuul:rolevar:: epel

      .. zuul:rolevar:: url

         The URL for an EPEL mirror.

   .. zuul:rolevar:: opensuse

      .. zuul:rolevar:: url

         The URL for an openSUSE mirror.

   .. zuul:rolevar:: debian
      :type: list

      A list of dictionaries, one for each Debian mirror URL.  This
      accomodates mirror systems which may have a security mirror at a
      different URL.

      .. zuul:rolevar:: url

         The URL for a Debian mirror.

      .. zuul:rolevar:: components
         :type: list

         A list of components available in this mirror (e.g.,
         ``main``, ``contrib``).

      .. zuul:rolevar:: trusted
         :default: False

         Set to True in order to tag APT mirrors as trusted.

   .. zuul:rolevar:: ubuntu
      :type: list

      A list of dictionaries, one for each Ubuntu mirror URL.  This
      accomodates mirror systems which may have a security mirror at a
      different URL.

      .. zuul:rolevar:: url

         The URL for an Ubuntu mirror.

      .. zuul:rolevar:: components
         :type: list

         A list of components available in this mirror (e.g.,
         ``main``, ``contrib``).

      .. zuul:rolevar:: trusted
         :default: False

         Set to True in order to tag APT mirrors as trusted.

   .. zuul:rolevar:: dockerhub

      .. zuul:rolevar:: url

         The URL for a Docker Hub mirror.
