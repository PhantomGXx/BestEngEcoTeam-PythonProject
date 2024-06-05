# Engineering Economics Project BEET - Functions

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
DATA = []

def PF(N,I,F=1):
    # P = F(P/F,R,N)
    L = (1+I)**N
    return F / L

def FP(N,I,P=1):
    # F = P(F/P,R,N)
    L = (1+I)**N
    return P * L

def PA(N,I,A=1):
    # P = A(P/A,R,N)
    L = (1+I)**N
    return A * ( (L-1)/(I * L) )

def AP(N,I,P=1):
    # A = P(A/P,R,N)
    L = (1+I)**N
    return P * ( (I * L)/(L-1) )

def PAL(N,I,J,AL=1):
    if I!=J:
        L = (1-((1+J)**N)*((1+I)**-N))/(I-J)
    else:
        L = N / (1+I)
    return AL * L














