#!/bin/bash

EMAIL_ADDRESS=""
PASSWORD=""
OPTIONS="--cookies=on --keep-session-cookies --save-cookies=cookies.txt"
SATELLITE_IDENTIFIER="25544"
OUTPUT_FILE="ISS.txt"
URL="https://www.space-track.org/basicspacedata/query/class/tle_latest/NORAD_CAT_ID/$SATELLITE_IDENTIFIER/orderby/ORDINAL asc/limit/1/format/3le/metadata/false"

wget --post-data="identity=$EMAIL_ADDRESS&password=$PASSWORD&query=$URL" $OPTIONS 'https://www.space-track.org/ajaxauth/login' -O $OUTPUT_FILE
