Install javascript dependencies needed for a project

**Role Variables**

.. zuul:rolevar:: zuul_work_dir
   :default: {{ zuul.project.src_dir }}

   The directory to work in.

.. zuul:rolevar:: tox_constraints_file

   Path to a pip constraints file. Will set the
   ``UPPER_CONSTRAINTS_FILE`` environment variable.  Useful if npm
   ``postinstall`` runs tox.
