#!/bin/bash
echo $(date) start ${3:22:7} 1>&2
mkdir -p /work/dc007/dc007/qunoot/$1/$4
mkdir -p /tmp/qk/
#echo $1 $2 $3
uz $2 | tr -d '\r'|\
 awk '/^WARC-Type: response/||n=0,!NF&&++n==2'|\
 grep -Ea '^(WARC-Target-URI|Last-Modified): '|\
 sed ':a;N;/\nLast-Modified:/s/\n/\t/;ta;P;D' |\
 sed 's/WARC-Target-URI: //; s/Last-Modified: //; s/\tLast-Modified:.*//' > /tmp/qk/$3
igzip -c /tmp/qk/$3 > /work/dc007/dc007/qunoot/$1/$4/$3.gz && rm /tmp/qk/$3
echo $(date) end ${3:22:7} 1>&2
