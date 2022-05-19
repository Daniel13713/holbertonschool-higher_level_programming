#!/bin/bash
#Obtain only status code
curl -sX POST -H 'Content-Type: application/json' "$1" -d @"$2"
