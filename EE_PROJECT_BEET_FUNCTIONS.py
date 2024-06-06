# Engineering Economics Project BEET - Functions

import numpy as np
import pandas as pd
import sklearn.linear_model as lm

def P_F(N,I,F=1):
    # P = F(P/F,R,N)
    L = (1+I)**N
    return F / L

def F_P(N,I,P=1):
    # F = P(F/P,R,N)
    L = (1+I)**N
    return P * L

def P_A(N,I,A=1):
    # P = A(P/A,R,N)
    L = (1+I)**N
    return A * ( (L-1)/(I * L) )

def A_P(N,I,P=1):
    # A = P(A/P,R,N)
    L = (1+I)**N
    return P * ( (I * L)/(L-1) )

def P_AL(N,I,J,AL=1):
    if I!=J:
        L = (1-((1+J)**N)*((1+I)**-N))/(I-J)
    else:
        L = N / (1+I)
    return AL * L

def NPV(CASH,I):
    # Net Present Value
    npv = 0
    for n,cash in enumerate(CASH):
        npv += cash / (1+I) ** n
    return npv












