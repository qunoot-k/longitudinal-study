#!/bin/bash
# Usage: sbatch [slurm args] .../simpleJob.sh script-name [script-args]

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --account=ec184-guest
#SBATCH --time=00:03:00
#SBATCH --job-name=tabulate
#SBATCH --output=log/launch_%j.out

echo $(date) startLaunch
export W=/work/dc007/dc007
year=$1
start_seg=$2
seg_per_task=$3
srun -c $SLURM_CPUS_PER_TASK $W/shared/qk/long*/com*/sort.sh $year $start_seg $seg_per_task
echo $(date) endLaunch

