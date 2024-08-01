#!/bin/bash
echo $(date) startFile $4 1>&2

input_file=$1
output_file=$2
err_file=$3
file_name=$4

uz $input_file | grep -Ea $'\t' |\
 python3 /work/dc007/dc007/shared/qk/long*/tim*/tabulate.py > /tmp/qk/$file_name".tsv" 2>/tmp/qk/$file_name"-err.tsv"

mv /tmp/qk/$file_name".tsv"  $output_file
mv /tmp/qk/$file_name"-err.tsv" $err_file

echo $(date) endFile $4 1>&2
