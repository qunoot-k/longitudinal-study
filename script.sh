#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME
files_per_task=$5
start_file_num=$6
task=$(((${SLURM_PROCID}*$files_per_task)+$start_file_num))
counter=0
for file_num in $(seq $task $(($task + $files_per_task - 1)))
do
	file_num=$(printf %04d $file_num)
	input_file=$1$2"/*."$3$4"*"$file_num".warc.gz"
	output_file=$2"-"$3"-"$file_num".tsv"
	$W/shared/bin/sing $W/shared/qk/slurm/createPair.sh $2 $input_file $output_file $3 &
	counter=$(($counter+1))
	if [[ $counter%8 -eq 0 ]]
	then
		wait
	fi
done
wait
echo $(date) endTask ${SLURM_PROCID}
