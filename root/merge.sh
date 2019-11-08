#! /bin/sh

# replace var from env
/bin/sed -i \
	"s/REPLACE_RELEASE_NAME/$RELEASE_TAG/g" \
	/buildout/endpoints.template
	
# merge yaml
/usr/bin/python3 /merge.py /buildout/endpoints.yml /buildout/endpoints.template
