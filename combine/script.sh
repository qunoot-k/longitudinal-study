#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

year=$1
start_seg=$2
num_of_seg=$3
counter=0
prefix=/work/dc007/dc007/qunoot/
#mkdir -p /tmp/qk
mkdir -p $prefix$year/combined

for segment in $(seq $start_seg $(($start_seg + $num_of_seg)))
	do
		cat $prefix$year/timestamp/$segment/* | sort -k5 > $prefix$year/combined/$segment.tsv &
		counter=$(($counter+1))
		if [[ $counter%8 -eq 0 ]]
			then
				wait
			fi
	done
wait

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

