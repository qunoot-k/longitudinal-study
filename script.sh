#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

prefix=$1
year=$2
start_seg=$3
suffix=$4
files_per_task=$5
start_file_num=$6
num_of_seg=$7
counter=0
task=$(((${SLURM_PROCID}*$files_per_task)+$start_file_num))
mkdir -p /tmp/qk/

for segment in $(seq $start_seg $(($start_seg + $num_of_seg)))
	do
		mkdir -p /work/dc007/dc007/qunoot/$year/$segment
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
	done
wait

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

