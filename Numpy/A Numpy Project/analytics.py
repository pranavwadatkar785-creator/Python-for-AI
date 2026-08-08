import numpy as np

def average(data):
    return np.average(data[:,1:5], axis=1)

def percentage(data):
    return ((np.sum(data[:,1:5], axis=1))/400)*100

def max_percentage(data):
    per = np.argmax(percentage(data))
    return data[per,0]