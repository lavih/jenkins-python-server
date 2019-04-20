#!/bin/sh
set -e
sleep 15
curl 127.0.0.1:1729 
exec "$@"
#add the log path