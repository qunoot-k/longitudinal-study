#!/bin/bash
# Usage: sbatch [slurm args] .../simpleJob.sh script-name [script-args]

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --account=ec184-guest
#SBATCH --time=00:03:00
#SBATCH --job-name=longitudinal_study
#SBATCH --output=log/launch_%j.out

echo $(date) startLaunch
export W=/work/dc007/dc007
prefix=/beegfs/common_crawl/CC-MAIN-
year=$1
segment=$2
suffix=/orig/warc/
files_per_task=$3
start_file_num=$4
srun -c $SLURM_CPUS_PER_TASK $W/shared/qk/longitudinal-study/script.sh $prefix $year $segment $suffix $files_per_task $start_file_num
echo $(date) endLaunch

