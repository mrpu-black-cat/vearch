#!/usr/bin/env bash
VERSION=latest
ROOT=`dirname ${PWD}`

function get_version() {
  VEARCH_VERSION_MAJOR=`cat ${ROOT}/VERSION | grep VEARCH_VERSION_MAJOR | awk -F' ' '{print $2}'`
  VEARCH_VERSION_MINOR=`cat ${ROOT}/VERSION | grep VEARCH_VERSION_MINOR | awk -F' ' '{print $2}'`
  VEARCH_VERSION_PATCH=`cat ${ROOT}/VERSION | grep VEARCH_VERSION_PATCH | awk -F' ' '{print $2}'`

  VERSION="${VEARCH_VERSION_MAJOR}.${VEARCH_VERSION_MINOR}.${VEARCH_VERSION_PATCH}"
  echo "VERSION="${VERSION}
}

get_version
docker run --privileged -i -v $(dirname "$PWD"):/vearch vearch/vearch_env:latest /vearch/cloud/compile/compile.sh
