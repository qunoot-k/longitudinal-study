#!/bin/bash
# Usage: sbatch [slurm args] .../simpleJob.sh script-name [script-args]

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --account=ec184-guest
#SBATCH --time=01:30:00
#SBATCH --job-name=longitudinal_study
#SBATCH --output=log/launch_%j.out

echo $(date) startLaunch
export W=/work/dc007/dc007
srun -c $SLURM_CPUS_PER_TASK $W/shared/qk/long*/year*/script.sh
echo $(date) endLaunch

