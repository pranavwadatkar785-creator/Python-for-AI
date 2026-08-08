import numpy as np

def average(data):
    return np.mean(data[:, 1:5], axis=1)

def percentage(data):
    return np.sum(data[:, 1:5], axis=1) / 4

def top_student(data):
    avg = average(data)
    index = np.argmax(avg)

    return data[index, 0], avg[index]

def bottom_student(data):
    avg = average(data)
    index = np.argmin(avg)

    return data[index, 0], avg[index]

def top_n_students(data, n):
    avg = average(data)
    indices = np.argsort(avg)[-n:][::-1]

    return data[indices, 0], avg[indices]

def subject_toppers(data):
    marks = data[:, 1:5]
    indices = np.argmax(marks, axis=0)

    return data[indices, 0]