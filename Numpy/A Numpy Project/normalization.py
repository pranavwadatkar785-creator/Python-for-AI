import numpy as np

def min_max_scale(data):
    min_val = np.min(data[:, 1:], axis=0)
    max_val = np.max(data[:, 1:], axis=0)
    scaled_data = (data[:, 1:] - min_val) / (max_val - min_val)
    return np.hstack((data[:, 0].reshape(-1,1), scaled_data))

def standardize(data):
    features = data[:, 1:]
    mean_val = np.mean(features, axis=0)
    std_val = np.std(features, axis=0)

    standardized = (features - mean_val) / std_val
    return standardized