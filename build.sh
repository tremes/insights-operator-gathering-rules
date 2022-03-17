#!/bin/bash

mkdir -p ./build

# Build the conditions
VERSION=$(git describe --tags --abbrev=0)
jq --arg VERSION $VERSION \
    -s '{ version: $VERSION, rules: map(.) }' ./conditions/*.json > ./build/rules.json
