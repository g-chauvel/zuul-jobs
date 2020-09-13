Ensure specified python interpreter and development files are installed

.. note:: This role is only available for Debian based platforms
          currently.

There are three ways to install the python interpreter:

1. Using distribution packages: This is the default (``python_use_pyenv`` and
   ``python_use_stow`` are both false``).

2. Install using ``pyenv``.

3. Install using ``stow``.

.. note:: You cannot use both ``pyenv`` and ``stow`` method for the same job.
          That means that ``python_use_pyenv`` and ``python_use_stow``
          cannot be set both to ``True`` at the same time.

**Role Variables**

.. zuul:rolevar:: python_version

   Optional version of python interpreter to install, such as ``3.7``.

.. zuul:rolevar:: python_use_pyenv
   :default: False

   Whether to optionally use ``pyenv`` to install python instead of distro
   packages.

.. zuul:rolevar:: python_use_stow
   :default: False

   In case you have image with already prepared python versions, for example used the
   python-stow-versions element, you can activate them with stow utility
   by setting this variable to ``true``.

.. zuul:rolevar:: python_stow_dir
   :default: /usr/local/stow

   Sets the target directory for stow. This should be the path to the
   directory where prepared python packages are located.
