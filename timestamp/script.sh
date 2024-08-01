#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

year=$1
start_seg=$2
files_per_task=$3
start_file_num=$4
num_of_seg=$5
counter=0
task=$(((${SLURM_PROCID}*$files_per_task)+$start_file_num))
mkdir -p /tmp/qk/
prefix=/work/dc007/dc007/qunoot/
for segment in $(seq $start_seg $(($start_seg + $num_of_seg)))
	do
		mkdir -p $prefix$year/timestamp/$segment
		mkdir -p $prefix$year/err/$segment
		for file_num in $(seq $task $(($task + $files_per_task - 1)))
		do
			file_num=$(printf %04d $file_num)
			file_name=$year"-"$segment"-"$file_num
			input_file=$prefix$year"/raw/"$segment"/"$file_name".tsv.gz"
			err_file=$prefix$year"/err/"$segment"/"$file_name".tsv"
			output_file=$prefix$year"/timestamp/"$segment"/"$file_name".tsv"
			$W/shared/bin/sing $W/shared/qk/lon*/tim*/createTable.sh $input_file $output_file $err_file $file_name
			counter=$(($counter+1))
			if [[ $counter%8 -eq 0 ]]
			then
				wait
			fi
		done
	done
wait

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

