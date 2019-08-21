An ansible role to install kubernetes.

**Role Variables**

.. zuul:rolevar:: install_kubernetes_with_cluster
   :default: True

   If true, installs a Minikube cluster.

.. zuul:rolevar:: minikube_version
   :default: latest

   The version of Minikube to install.

.. zuul:rolevar:: minikube_dns_resolvers
   :default: []

   List of dns resolvers to configure in k8s. Use this to override the
   resolvers that are found by default.
