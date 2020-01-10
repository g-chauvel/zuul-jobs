Run Helm by templating the chart, it assumes that a Kubernetes cluster is
already setup and the Helm executable is installed.

**Role Variables**

.. zuul:rolevar:: helm_release_name

   Helm release name (mandatory)

.. zuul:rolevar:: helm_chart

   Directory of the Helm chart.

.. zuul:rolevar:: zuul_work_dir
   :default: {{ zuul.project.src_dir }}

   Directory to run go in.
