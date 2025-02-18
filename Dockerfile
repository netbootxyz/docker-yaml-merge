FROM alpine:3.21

RUN \
 echo "**** install build packages ****" && \
 apk add --no-cache --upgrade --virtual=build-dependencies \
	py3-pip \
	python3-dev && \
 rm /usr/lib/python*/EXTERNALLY-MANAGED && \
 echo "**** install packages ****" && \
 apk add --no-cache \
	python3 && \
 echo "**** install pip packages ****" && \
 pip3 install -U \
	hiyapyco \
	markupsafe==2.1.5 && \
 echo "**** directories ****" && \
 mkdir -p \
	/buildout && \
 echo "**** clean up ****" && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/root/.cache \
	/tmp/*

# add local files
COPY /root /

ENTRYPOINT [ "/merge.sh" ]
