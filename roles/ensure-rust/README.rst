Install Rust

Install the Rust toolchain

**Role Variables**

.. zuul:rolevar:: ensure_rust_rustup
   :default: True

   Install Rust via the ``rustup`` installer.

.. zuul:rolevar:: ensure_rust_rustup_toolchain
   :default: stable

   The Rust toolchain to install with ``rustup``.

.. zuul:rolevar:: ensure_rust_rustup_path
   :default: /usr

   Where to install Rust/Cargo with ``rustup``.  ``/usr`` provides the
   tools globally.  This may conflict with distribution Rust packages
   if installed.

.. zuul:rolevar:: ensure_rust_packages
   :default: False

   Install Rust via system packages.  This role does not currently
   support package install.
