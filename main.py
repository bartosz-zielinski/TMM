import pandas
from utils import *
from numpy import linspace


#INPUT DATA FOR OPTIMIZATION
max_layer_number = 20 #maximal number of thin film layers
max_layer_thickness = 50 # maximal layer thickness in nm
max_layer_thickness_step = 10 # layer step increment in nm 
min_layer_thickness = 0 # minimal layer thickness = thinner layers are going to get diregarded 
av_materials = ["ZnO","Al2O3","TiO2"] #available materialas
superstrate = "Air" #incident semiinfinite medium
substrate = "Low Iron Glass" #outgoing semiinfinite medium
lambda_list = linspace(300,1200,91) # wavelengths in nm


results=BruteForceOptimize(superstrate,substrate,min_layer_thickness,max_layer_thickness,max_layer_thickness_step,max_layer_number,av_materials,lambda_list)
out = pandas.DataFrame({'design_no' : results[0], 'design_str' : results[1], 'design_J[mA/cm2]' : results[2]})
out.to_csv('out.csv')









