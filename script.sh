#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

prefix=$1
year=$2
segment=$3
suffix=$4
files_per_task=$5
start_file_num=$6

mkdir -p /work/dc007/dc007/qunoot/$year/$segment
mkdir -p /tmp/qk/

task=$(((${SLURM_PROCID}*$files_per_task)+$start_file_num))
counter=0
for file_num in $(seq $task $(($task + $files_per_task - 1)))
do
	file_num=$(printf %04d $file_num)
	input_file=$prefix$year"/*."$segment$suffix"*"$file_num".warc.gz"
	output_file=$year"-"$segment"-"$file_num".tsv"
	$W/shared/bin/sing $W/shared/qk/longitudinal-study/createPair.sh $year $input_file $output_file $segment &
	counter=$(($counter+1))
	if [[ $counter%8 -eq 0 ]]
	then
		wait
	fi
done
wait

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

