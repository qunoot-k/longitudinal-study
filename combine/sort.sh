#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

year=$1
start_seg=$2
seg_per_task=$3
counter=0
prefix=/work/dc007/dc007/qunoot/
#mkdir -p /tmp/qk
task=$(((${SLURM_PROCID}*$seg_per_task)+$start_seg))
for segment in $(seq $task $(($task + $seg_per_task - 1)))
	do
		$W/shared/qk/long*/com*/filesort.sh $segment $prefix$year/com*/$segment.tsv &
		counter=$(($counter+1))
		if [[ $counter%8 -eq 0 ]]
			then
				wait
			fi
	done
wait

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

