Ensure tox is installed

Look for ``tox``, and if not found, install it via ``pip`` in the user
install directory (i.e., ``pip install --user``).

After running this role, ``tox_executable`` will be set as the path to
a valid ``tox``.

**Role Variables**

.. zuul:rolevar:: tox_executable
   :default: ``tox``

   Look for an existing ``tox`` at this specific path.  Note the
   default (``tox``) effectively means to find tox in the current
   ``$PATH``.

.. zuul:rolevar:: tox_prefer_python2
   :default: ``false``

   If tox is not detected, prefer to install tox inside Python 2
   instead of Python 3.

   If set,
   :zuul:rolevar:`ensure-pip.ensure_pip_from_packages_with_python2`
   will be automatically set to `True` to enable a Python 2
   installation of `pip`.
