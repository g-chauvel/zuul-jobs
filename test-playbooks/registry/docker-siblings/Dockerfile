FROM docker.io/upstream/image as first
ARG ZUUL_SIBLINGS=""
RUN echo "Zuul siblings: ${ZUUL_SIBLINGS}"
RUN cp /test-nonce /test-nonce-is-there
COPY .zuul-siblings/opendev.org/project/fake-sibling/file /target
COPY .zuul-siblings/openstack.org/project/fake-sibling/file /target
CMD echo "Zuul container test"; sleep infinity

FROM first as second
RUN echo "This is just to test that loops with siblings work"
