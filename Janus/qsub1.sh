#!/bin/bash
#PBS -N WorkFlow1
#PBS -q database
#PBS -l select=1:ncpus=28:mpiprocs=112
#PBS -l walltime=720:00:00
#PBS -j oe
#PBS -V

module load MyModules/QE-6.4
module load MyModules/anaconda3

cd /opt/home/Himanshu/DataBaseProject/Janus/1-1.5
#pwd
python RunWorkflow.py
cd ..

cd /opt/home/Himanshu/DataBaseProject/Janus/2.5-3
#pwd
python RunWorkflow.py
cd ..
