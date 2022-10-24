from __future__ import division, print_function, absolute_import
from cProfile import label
from calendar import c
import math
from numpy import pi, linspace, inf, array
from tmm import (coh_tmm, unpolarized_RT, ellips,position_resolved, find_in_structure_with_inf)
from models.materials import Material
import matplotlib.pyplot as plt
import pandas as pd


# pip install tmm


def CalculateReflection(lambda_vec,mat_list,d_list):
    R_list=[]
    for vwl in lambda_vec:
        n_list=[]
        
        for mat in mat_list:
            n_list.append(mat.get_RI(vwl))
        
        R=unpolarized_RT(n_list,d_list,0,vwl)['R']
        R_list.append(R)

    return R_list

layer_thickness = [109,] # layer thickness in nm
layer_material = Material("ZnOcrystal") #material layer name
#layer_material2 = Material("ZnO") #material layer name
superstrate = Material("Air") #incident semi-infinite medium
substrate = Material("Si") #outgoing semi-infinite medium

mat_list = [superstrate,layer_material,substrate]
d_list = [inf,layer_thickness,inf]
lambda_list = linspace(300,1200,901) # wavelengths in nm

#mat_list2 = [superstrate,layer_material2,substrate]



#calculated_R2 = CalculateReflection(lambda_list, mat_list2, d_list)
measured_R=[]
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_1.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_4.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_7.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_10.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_13.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_sz_16.csv", skiprows=19,skipfooter=45,header=None, engine="python"))

measured_R.append(pd.read_csv("probki\csv\ZnO_B19_1.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
measured_R.append(pd.read_csv("probki\csv\ZnO_B19_2.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
measured_R.append(pd.read_csv("probki\csv\ZnO_B19_3.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
measured_R.append(pd.read_csv("probki\csv\ZnO_B19_4.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
measured_R.append(pd.read_csv("probki\csv\ZnO_B19_5.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_6.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_7.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_8.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_9.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_10.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_11.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_12.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_13.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_14.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_15.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.append(pd.read_csv("probki\csv\ZnO_B19_16.csv", skiprows=19,skipfooter=45,header=None, engine="python"))
#measured_R.set_index("lambda","R")
#measured_R.sort_values(by="1200.0000")

#print(measured_R.columns)
#print(calculated_R[0])

#plt.plot(lambda_list,calculated_R)
for thickness in layer_thickness:
    result=CalculateReflection(lambda_list, mat_list, [inf,thickness,inf])
    plt.plot(lambda_list,result)

for spec in measured_R:
    plt.plot(spec[0],spec[1])
plt.xlim([300, 1200])
plt.xlabel('wavelength [nm]')
plt.ylabel('R [a.u.]')
plt.show()