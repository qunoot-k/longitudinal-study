#!/bin/bash
# Usage: sbatch [slurm args] .../simpleJob.sh script-name [script-args]

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --account=ec184-guest
#SBATCH --time=01:30:00
#SBATCH --job-name=longitudinal_study
#SBATCH --output=launch_%j.out

export W=/work/dc007/dc007
srun -c $SLURM_CPUS_PER_TASK $W/shared/bin/sing python3 $W/shared/qk/long*/year*/corr.py

