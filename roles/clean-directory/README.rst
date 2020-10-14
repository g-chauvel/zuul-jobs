Clean a directory, but leave the directory alone

This is the equivalent of ``rm -rf *`` when run in a directory.  It is
safe to run in executor context.

**Role Variables**

.. zuul:rolevar:: clean_directory_path

   The directory to clean.
