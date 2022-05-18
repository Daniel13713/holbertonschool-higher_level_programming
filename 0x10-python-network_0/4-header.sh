#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL
curl -siH 'X-HolbertonSchool-User-Id: 98' "$1" | tail -1 | awk 'printf "%s %s", $1,$3'
