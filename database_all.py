import numpy as np
import pandas as pd

### Flip the airfoil data
# data = pd.read_csv("AirfoilData.csv")
# data_array=np.array(data)
# data_flip=np.flip(data_array,axis=1)
# data_flip_frame=pd.DataFrame(data_flip)
# data_flip_frame.to_csv("AirfoilDataFlip.csv")
#### getting negative the "Cl" for flipped airfoils
# data2=pd.read_csv("ReAlphaCl.csv")
# data2_array=np.array(data2)
# data2_array[:,2] = -data2_array[:,2]
# data2_flip_frame=pd.DataFrame(data2_array)
# data2_flip_frame.to_csv("ReAlphaClFlip.csv")
### AirfoilDataAll = AirfoilData + AirfoilDataFlip
# AirfoilData=pd.read_csv("AirfoilData.csv")
# AirfoilDataFlip=pd.read_csv("AirfoilDataFlip.csv")
# AirfoilDataAll = np.concatenate(([AirfoilData] + [AirfoilDataFlip]), axis=0)
# AirfoilDataAll_frame=pd.DataFrame(AirfoilDataAll)
# AirfoilDataAll_frame.to_csv("AirfoilDataAll.csv")
# ### ReAlphaClAll = ReAlphaCl + ReAlphaClFlip
# ReAlphaCl=pd.read_csv("ReAlphaCl.csv")
# ReAlphaClFlip=pd.read_csv("ReAlphaClFlip.csv")
# ReAlphaClAll = np.concatenate(([ReAlphaCl] + [ReAlphaClFlip]), axis=0)
# ReAlphaClAll_frame=pd.DataFrame(ReAlphaClAll)
# ReAlphaClAll_frame.to_csv("ReAlphaClAll.csv")
### DatabaseAll = AirfoilDataAll + ReAlphaClAll
# AirfoilDataAll=pd.read_csv("AirfoilDataAll.csv")
# ReAlphaClAll=pd.read_csv("ReAlphaClAll.csv")
# DatabaseAll = np.concatenate(([AirfoilDataAll] + [ReAlphaClAll]), axis=1)
# DatabaseAll_frame=pd.DataFrame(DatabaseAll)
# DatabaseAll_frame.to_csv("DatabaseAll.csv")
