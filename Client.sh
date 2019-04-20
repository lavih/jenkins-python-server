#!/bin/sh
set -e
sleep 15
curl python-server:1729 
exec "$@"
#add the log path