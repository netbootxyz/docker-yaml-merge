# docker-yaml-merge

The purpose of this container is to merge a local template with a remote settings yaml file based on a unique version number that our repo just released.
This is a helper container for a larger build and release pipeline.

Usage Snippet:

```
docker run --rm -it \
  -e RELEASE_TAG=your_release_tag \
  -v $(pwd):/buildout \
  netbootxyz/yaml-merge
```
