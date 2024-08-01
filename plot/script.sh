#!/bin/bash
echo $(date) startTask ${SLURM_PROCID} $SLURMD_NODENAME

year=2019-35
#mkdir -p /tmp/qk
file=$((${SLURM_PROCID} + 1))
$W/shared/bin/sing python3 $W/shared/qk/long*/year*/split.py $file
echo $(date) endTask ${SLURM_PROCID} $SLURMD_NODENAME

