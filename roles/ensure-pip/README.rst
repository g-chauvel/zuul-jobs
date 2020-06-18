Ensure pip is available

This role is intended install the requirements for the `pip module
<https://docs.ansible.com/ansible/latest/modules/pip_module.html>`__
on hosts.

Jobs that also wish to call ``pip`` via shell commands directly can
also use this to ensure ``pip`` is available.  However, it should be
noted that calling ``pip`` is ambiguous when supporting many
platforms.  On some platforms it may install the package under the
Python 2 interpreter and in others Python 3.  You should use a
qualified name (``pip2`` or ``pip3``) to avoid confusion.

This role will also install ``wheel`` components sufficient to run
``bdist_wheel`` builds or ``pip wheel`` on a source tree.

**Role Variables**

.. zuul:rolevar:: ensure_pip_from_packages
   :default: True

   Ensure the system packages for pip with the running
   ``ansible_python_interpreter`` are installed.

.. zuul:rolevar:: ensure_pip_from_packages_with_python2
   :default: False

   Also ensure Python 2 pip is available.  This is for backwards
   compatability with platforms that have
   ``ansible_python_interpreter`` as Python 3 but may run some jobs
   that still require Python 2 libraries.  Note that this may bring in
   the Python 2 interpreter environment, which may not be desirable or
   even available on many platforms.

.. zuul:rolevar:: ensure_pip_from_upstream
   :default: False

   Install pip from latest upstream sources locally.  Note this is
   probably not what you want and should be used with extreme caution.
   The installed pip does not coordinate with the system packaged
   versions, and can lead to wide variety of problems if CI jobs
   re-install ``pip`` packages, for example.

.. zuul:rolevar:: ensure_pip_from_upstream_interpreters
   :default: [ ansible_python_interpreter ]

   A list of interpreters to install pip from upstream with.  Note
   that by default the *last* entry in the list will likely own the
   ``/usr/local/bin/pip`` command; this can create confusion for
   legacy jobs if they assume ``pip`` installs Python 2 libraries but
   it is actually installing into the Python 3 environment.  This role
   does not install the Python 2 interpreter, which may not be
   available on the system, so caution should be used when specifying
   ``python2`` in this list.

**Output Variables**

.. zuul:rolevar:: ensure_pip_virtualenv_cmd

   This variable will be set to a command appropriate for general
   usage with the ``pip`` module ``virtualenv_command`` argument on the
   host.  On Python 3 hosts this will be the inbuilt ``venv`` module, on
   Python 2 hosts the ``virtualenv`` package will be installed (this is
   avoided on Python 3 hosts as an unnecessary dependency).
