Validate bind zone.db files

This role uses ``named-checkzone`` to validate Bind ``zone.db`` files.

**Role Variables**

.. zuul:rolevar:: zone_files
   :default: zuul.project.src_dir

   Look for ``zone.db`` files recursively in this directory.  The
   layout should be ``domain.xyz/zone.db`` where a parent directory is
   named for the zone the child ``zone.db`` file describes.
