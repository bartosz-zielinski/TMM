from __future__ import division, print_function, absolute_import
from cProfile import label
from calendar import c
import math
from numpy import pi, linspace, inf, array
from tmm import (coh_tmm, unpolarized_RT, ellips,position_resolved, find_in_structure_with_inf)
import sqlite3
import sys,os
from utils.populate import Populate
from models.materials import Material
from models.spectrums import Spectrum
from models.spectral_response import IQE
from multiprocessing import Process

clear=lambda:os.system('cls')

def CalculateCurrent(lambda_vec,spectrum,SR,T):
    wvl1 = 0
    Jsc = 0
    for wvl,tr in zip(lambda_vec, T):
        wvl2 = wvl
        dwvl = wvl2-wvl1
        Jsc = Jsc+spectrum.get_Intensity(wvl) * wvl/1239.8 *SR.get_IQE(wvl)* tr * dwvl
        wvl1 = wvl2
    return Jsc/10 #mA/cm2

def CalculateTransmission(lambda_vec,mat_list,d_list):
    T_list=[]
    for vwl in lambda_vec:
        n_list=[]
        
        for mat in mat_list:
            n_list.append(mat.get_RI(vwl))
        
        T=unpolarized_RT(n_list,d_list,0,vwl)['T']
        T_list.append(T)

    return T_list

def CalculateReflection(lambda_vec,mat_list,d_list):
    R_list=[]
    for vwl in lambda_vec:
        n_list=[]
        
        for mat in mat_list:
            n_list.append(mat.get_RI(vwl))
        
        R=unpolarized_RT(n_list,d_list,0,vwl)['R']
        R_list.append(R)

    return R_list

def BruteForceOptimize(superstrate,substrate,min_layer_thickness,max_layer_thickness,step,max_layer_number,materials,lambda_list):
    designs = Populate(superstrate, substrate, min_layer_thickness, max_layer_thickness, step, max_layer_number, materials)
    out_No=[]
    out_Jsc=[]
    out_design=[]
    out_impr=[]

    i = 0
    l = len(designs)

    start = time.time()
    clear()

    for design in designs:
        i=i+1
        T=CalculateTransmission(lambda_list, design["m_list"], design["d_list"])
        
        tmp='['
        for mat,thick in zip(design["m_list"], design["d_list"]):
            tmp=tmp+str(thick)+' nm'+' '+mat.formula+' | '
        
        out_design.append(tmp+']')
        out_Jsc.append(CalculateCurrent(lambda_list, Spectrum('AM1.5'), IQE('IBC_cell'), T))
        out_No.append(i)

    return [out_No,out_design,out_Jsc]
    