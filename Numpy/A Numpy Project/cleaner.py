import numpy as np

def missing_val(data):
    return np.isnan(data).sum(axis=0)

def duplicate(data):
    uni, counts = np.unique(data[:,0], return_counts=True)
    dup = uni[counts>1]
    return dup

def invalid(data):
    marks = data[:,1:]
    return (marks<0) | (marks>100)

def handle_missing(data, choice):
    if choice == 1:
        data[np.isnan(data)] = 0
    else:
        data_mean = np.nanmean(data, axis=0)
        # mask = np.isnan(data)
        # data[mask] = np.broadcast_to(data_mean, data.shape)[mask]
        data = np.where(np.isnan(data), data_mean, data)
    return data

def handling_duplicates(data):
    _, indices = np.unique(data[:,0], return_index=True)
    clean_data = data[indices]
    data = clean_data
    return data

def fix_invalids(data):
    marks = data[:,1:]

    marks[marks< 0 ] = 0
    marks[marks> 100] = 100
    return data

