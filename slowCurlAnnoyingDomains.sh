#!/bin/bash
#
FILE=$1
exec 3<&0
exec 0<$FILE
while read line
do
        curl --connect-timeout 4 -w "%{url_effective}\n" -I -L -s -S $line -o /dev/null >> results.txt
        printf "testing %s\n" "$line"
done
exec 0<&3
