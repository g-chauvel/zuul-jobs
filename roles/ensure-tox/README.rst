Ensure tox is installed

If tox is not already installed, it will be installed via pip in the
user install directory (i.e., "pip install --user").

**Role Variables**

.. zuul:rolevar:: tox_executable
   :default: ``tox``

   Optional path to point tox executable

.. zuul:rolevar:: tox_prefer_python2
   :default: ``true``

   If tox is not detected, prefer to install tox inside Python 2 instead of
   Python 3.
