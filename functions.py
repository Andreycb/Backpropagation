import math
import csv
import os

def Sigmoid(t):
  return 1 / (1 + math.exp(-t))

def TangHiper(t):
  return 1 / (1 + math.exp(2*-t))

def DerSigmoid(t):
    return math.exp(-t) / ( (1 + math.exp(-t)) * (1+math.exp(-t)) )

def DerTangHiper(t):
    return 1-(TangHiper(t)**2)

def ErrorNetwork(error_output, network_error):
    
    soma = 0
    er = 0
    while er < network_error:
        soma += error_output[er] * error_output[er]

    return soma/2

