Download and install Bazel, if the specified version is not already present.

**Role Variables**

.. zuul:rolevar:: bazel_version
   :default: '3.1.0'

   The version of Bazel required.

.. zuul:rolevar:: bazel_release_url
   :default: 'https://github.com/bazelbuild/bazel/releases/download'

   The base URL to use when downloading Bazel releases.
