# Engineering Economics Project BEET - Functions

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
DATA = []

def PF(F,R : float ,N):
    # P = F(P/F,R,N)
    L = (1+R)**N
    return F / L

def FP(P,R : float ,N):
    # F = P(F/P,R,N)
    L = (1+R)**N
    return P * L

def PA(A,R : float ,N):
    # P = A(P/A,R,N)
    L = (1+R)**N
    return A * ( (L-1 )/(R * L) )

def AP(P,R : float ,N):
    # A = P(A/P,R,N)
    L = (1+R)**N
    return P * ( (R * L)/(L-1) )


















