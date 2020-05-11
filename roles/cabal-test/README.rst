Run the cabal test command.

**Role Variables**

.. zuul:rolevar:: cabal_target

   The cabal target(s) to test.

.. zuul:rolevar:: zuul_work_dir
   :default: {{ zuul.project.src_dir }}

   Directory to run the cabal command in.
