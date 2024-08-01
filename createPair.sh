#!/bin/bash
echo $(date) startFile ${3:22:7} $3 1>&2

year=$1
input_file=$2
output_file=$3
segment=$4

uz $input_file | tr -d '\r'|\
 awk '/^WARC-Type: response/||n=0,!NF&&++n==2'|\
 grep -Ea '^(WARC-Target-URI|Last-Modified): '|\
 sed ':a;N;/\nLast-Modified:/s/\n/\t/;ta;P;D' |\
 sed 's/WARC-Target-URI: //; s/Last-Modified: //; s/\tLast-Modified:.*//' > /tmp/qk/$output_file

igzip -c /tmp/qk/$output_file > /work/dc007/dc007/qunoot/$year/$segment/$output_file.gz && rm /tmp/qk/$output_file

echo $(date) endFile ${3:22:7} $output_file 1>&2
