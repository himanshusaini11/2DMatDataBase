#!/bin/bash
#PBS -N WorkFlow1Test
#PBS -q res-1
#PBS -l select=2:ncpus=28:mpiprocs=16
#PBS -l walltime=720:00:00
#PBS -j oe
#PBS -V

module load MyModules/QE-6.3
module load MyModules/anaconda3

cd /opt/home/Himanshu/DataBaseProject/MX2
python MX2Workflow.py
