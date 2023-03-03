########################################################################
########################################################################
"""
xemora_pipe.py 

Title: Unpublished work

By: H. Kawabe, N. Kaplan, J. A. Marchand

Updated: 3/2/23
"""
########################################################################
########################################################################


import os
import glob
import sys
from pathlib import Path
from lib.xr_tools import *
from lib.xr_params import *



############################################################
#Training paths
working_dir = '~/xenomorph/bishop-dev/test_xemora/' 
xna_fast5_dir = '~/DataAnalysis/Marchand/221124_PZ_libv2'
xna_ref_fasta = 'ref/ref_libv2_PZ_AxBx-.fa'
dna_fast5_dir = '~/DataAnalysis/Marchand/230121_BSn_libv2_AB'
dna_ref_fasta = 'ref/ref_libv2_PZ_AxBx-.fa'
############################################################

############################################################
#Base calling paths 
bc_working_dir = '~/xenomorph/bishop-dev/p_basecall_test_2/' 
bc_fast5_dir = '~/DataAnalysis/Marchand/221124_PZ_libv2_200k'
bc_xna_ref_fasta = 'ref/ref_libv2_PZ_AxBx-.fa'
bc_model_file = '~/xenomorph/bishop-dev/test_xemora/model/model_best.pt'
############################################################

############################################################
train_model = False 
basecall_reads = True
############################################################



#Train dataset with xemora train
if train_model ==True: 
    cmd = 'python xemora.py train -w '+working_dir+' -f '+xna_fast5_dir +' '+dna_fast5_dir+' -r '+xna_ref_fasta+' '+dna_ref_fasta
    os.system(cmd)


#Basecall fast5 directory 
if basecall_reads==True: 
    cmd = 'python xemora.py basecall -w '+bc_working_dir+' -f '+bc_fast5_dir+' -r '+bc_xna_ref_fasta+' -m '+bc_model_file 
    os.system(cmd)

