import numpy as np

def calculate(list):
    x = np.array(list).reshape(3,3)
    Dict = dict()
    Dict['mean'] =[ [np.average(x[:,[0]]),np.average(x[:,[1]]),np.average(x[:,[2]])],[np.average(x[0]),np.average(x[1]),np.average(x[2])],np.average(x)]
    Dict['variance'] =[ [np.var(x[:,[0]]),np.var(x[:,[1]]),np.var(x[:,[2]])],[np.var(x[0]),np.var(x[1]),np.var(x[2])],np.var(x)]
    Dict['standard deviation'] =[ [np.std(x[:,[0]]),np.std(x[:,[1]]),np.std(x[:,[2]])],[np.std(x[0]),np.std(x[1]),np.std(x[2])],np.std(x)]
    Dict['max'] =[ [np.max(x[:,[0]]),np.max(x[:,[1]]),np.max(x[:,[2]])],[np.max(x[0]),np.max(x[1]),np.max(x[2])],np.max(x)]
    Dict['min'] =[ [np.min(x[:,[0]]),np.min(x[:,[1]]),np.min(x[:,[2]])],[np.min(x[0]),np.min(x[1]),np.min(x[2])],np.min(x)]
    Dict['sum'] =[ [np.sum(x[:,[0]]),np.sum(x[:,[1]]),np.sum(x[:,[2]])],[np.sum(x[0]),np.sum(x[1]),np.sum(x[2])],np.sum(x)]



    return Dict
