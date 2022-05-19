#!/bin/bash
#Obtain only status code
curl -sLX PUT "$1" -d user_id=98 -H "Origin: HolbertonSchool"
