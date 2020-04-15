Ensure tox is installed

Look for ``tox``, and if not found, install it via ``pip`` in the user
install directory (i.e., ``pip install --user``).

**Role Variables**

.. zuul:rolevar:: tox_prefer_python2
   :default: False

   If tox is not detected, prefer to install tox inside Python 2
   instead of Python 3.

   If set,
   :zuul:rolevar:`ensure-pip.ensure_pip_from_packages_with_python2`
   will be automatically set to `True` to enable a Python 2
   installation of `pip`.

**Output Variables**

.. zuul:rolevar:: tox_executable
   :default: tox

   After running this role, ``tox_executable`` will be set as the path
   to a valid ``tox``.

   At role runtime, look for an existing ``tox`` at this specific
   path.  Note the default (``tox``) effectively means to find tox in
   the current ``$PATH``.  For example, if your base image
   pre-installs tox in an out-of-path environment, set this so the
   role does not attempt to install the user version.
