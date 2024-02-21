#!/bin/bash
#PBS -N WorkFlow2
#PBS -q database
#PBS -l select=1:ncpus=8:mpiprocs=8
#PBS -l walltime=720:00:00
#PBS -j oe
#PBS -V

module load MyModules/QE-6.4
module load MyModules/anaconda3

cd /opt/home/Himanshu/DataBaseProject/Janus/1.5-2
python RunWorkflow.py
cd ..
