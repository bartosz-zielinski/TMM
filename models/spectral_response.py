import pandas as pd
from numpy import pi, linspace, inf, array
from scipy.interpolate import interp1d

#LOAD EXTERNAL DATA ALL AT ONCE
iqe_data=pd.read_json("json\iqe_data.json").set_index("name")

class IQE:
    def __init__(self,nm):
        self.name = nm
        self.description = iqe_data.loc[nm,"description"]
        self.wvl = iqe_data.loc[nm,"lambda"]
        self.IQE = iqe_data.loc[nm,"IQE"]
        self.get_iq =  interp1d(self.wvl,self.IQE)
        
    def get_IQE(self,wvl):
        return self.get_iq(wvl)
