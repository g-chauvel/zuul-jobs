Run the Haskell stack test command.

**Role Variables**

.. zuul:rolevar:: lts_version

   The lts version.

.. zuul:rolevar:: zuul_work_dir
   :default: {{ zuul.project.src_dir }}

   Directory to run the cabal command in.
