import numpy as np

def mean_marks(data):
    return np.nanmean(data[:,1:5], axis=0, )

def median_marks(data):
    return np.nanmedian(data[:,1:5], axis=0)

def max_marks(data):
    return np.nanmax(data[:,1:5], axis=0)

def min_marks(data):
    return np.nanmin(data[:,1:5], axis=0)

def variance_marks(data):
    return np.var(data[:,1:5], axis=0)

def std_deviation_marks(data):
    return np.std(data[:,1:5], axis=0)