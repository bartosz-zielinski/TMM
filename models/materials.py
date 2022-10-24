import pandas as pd
from numpy import pi, linspace, inf, array
from scipy.interpolate import interp1d
import sys,os

PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

#LOAD EXTERNAL DATA
material_data=pd.read_json("json\materials.json").set_index("formula")

class Material:
    def __init__(self,form):
        self.formula = form
        self.name = material_data.loc[form,"name"]
        self.description = material_data.loc[form,"description"]
        self.wvl = material_data.loc[form,"lambda"]
        self.n = material_data.loc[form,"n"]
        self.k = material_data.loc[form,"k"]
        self.get_n =  interp1d(self.wvl,self.n,fill_value="extrapolate")
        self.get_k = interp1d(self.wvl,self.k,fill_value="extrapolate") 
        
    def get_RI(self,wvl):
        return complex(self.get_n(wvl),self.get_k(wvl))