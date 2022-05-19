#!/bin/bash
#Obtain only status code
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
