Run nimble command in a source directory. Assumes the appropriate version of nim and nimble is installed.

**Role Variables**

.. zuul:rolevar:: nimble_command
   :default: build

   Nimble command to run.
   Examples are "build", "run" or "test".

.. zuul:rolevar:: nim_path

   Path where nim and nimble are installed.

.. zuul:rolevar:: zuul_work_dir
   :default: {{ zuul.project.src_dir }}

   Directory to run nimble in.
