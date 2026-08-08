import numpy as np

def load_data(filepath):
    data = np.genfromtxt(filepath,
                          delimiter=",",
                          skip_header=1,
                          filling_values=np.nan)
    return data
