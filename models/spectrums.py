import pandas as pd
from numpy import pi, linspace, inf, array
from scipy.interpolate import interp1d

#LOAD EXTERNAL DATA
spectrum_data=pd.read_json("json\spectrum.json").set_index("name")

class Spectrum:
    def __init__(self,nm):
        self.name = nm
        self.description = spectrum_data.loc[nm,"description"]
        self.wvl = spectrum_data.loc[nm,"lambda"]
        self.intensity = spectrum_data.loc[nm,"intensity"]
        self.get_i =  interp1d(self.wvl,self.intensity)
        
    def get_Intensity(self,wvl):
        return self.get_i(wvl)
        
