import numpy as np

def correlation_matrix(data):
    features = data[:, 1:]
    return np.corrcoef(features, rowvar=False)


def subject_correlation(data, subject1, subject2):
    return np.corrcoef(
        data[:, subject1],
        data[:, subject2]
    )[0, 1]


def correlation_with_average(data):
    features = data[:, 1:5]
    avg = np.mean(features, axis=1)

    return np.corrcoef(
        np.column_stack((features, avg)),
        rowvar=False
    )