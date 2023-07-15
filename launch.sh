#!/bin/bash
# Usage: sbatch [slurm args] .../simpleJob.sh script-name [script-args]

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --account=ec184-guest
#SBATCH --time=00:03:00
#SBATCH --job-name=testwarc
#SBATCH --output=trash/launch_%j_%t.out

echo $(date) startLaunch
export W=/work/dc007/dc007
prefix=/beegfs/common_crawl/CC-MAIN-
year=2019-35
segment=0
suffix=/orig/warc/
files_per_task=$1
start_file_num=$2
srun -c $SLURM_CPUS_PER_TASK $W/shared/qk/slurm/script.sh $prefix $year $segment $suffix $files_per_task $start_file_num
echo $(date) endLaunch

