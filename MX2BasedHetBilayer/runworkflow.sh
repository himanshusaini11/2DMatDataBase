#!/bin/bash
#PBS -N WorkFlowHet
#PBS -q work-02
#PBS -l select=1:ncpus=28:mpiprocs=28
##PBS -l walltime=720:00:00
#PBS -j oe
#PBS -V

module load MyModules/QE-6.3
module load MyModules/anaconda3

cd /opt/home/Himanshu/DataBaseProject/MX2BasedHetBilayer
python MX2-HETWorkflow.py
