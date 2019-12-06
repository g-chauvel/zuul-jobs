FROM docker.io/library/debian:testing
ARG ZUUL_SIBLINGS=""
RUN echo "Zuul siblings: ${ZUUL_SIBLINGS}"
COPY .zuul-siblings/opendev.org/project/fake-sibling/file /target
COPY .zuul-siblings/openstack.org/project/fake-sibling/file /target
CMD echo "Zuul container test"; sleep infinity
