#!/bin/bash
while :
do
        str=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8192)
        key=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 8192)
        rdcli -h "$1" set "$key" $str
done