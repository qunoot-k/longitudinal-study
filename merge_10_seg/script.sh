#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

year=$1
prefix=/work/dc007/dc007/qunoot/
#mkdir -p /tmp/qk
mkdir -p $prefix$year/merge_10_seg
segment=$2
#segment=${SLURM_PROCID}
cat $prefix$year/comb*/*$segment.tsv > $prefix$year/merge_10_seg/$segment.tsv &

echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

