Copy contents from ``{{ zuul.executor.work_root }}/artifacts/`` to AFS

**Role Variables**

.. zuul:rolevar:: afs_source

  Path to local source directory.

.. zuul:rolevar:: afs_target

  Target path in AFS (should begin with '/afs/...').

.. zuul:rolevar:: afs_copy_only
   :default: True

   If set to `false`, this will specify `--delete-after` to remove
   files on the remote side that do not exist on the copying side.
   When set to `true` will act as a regular additive copy process and
   will not remove any remote files.
