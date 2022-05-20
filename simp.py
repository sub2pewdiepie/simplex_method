from ast import Pass
import pandas as pd
import numpy as np


def simplex(data):
    # Basis = data.loc[:,:'Basis']
    # x = data.loc[:,'x1':'y1']
    # x = x.iloc[:,:-1]
    # y = data.loc[:, 'y1':'bi']
    # y = y.iloc[:, :-1]
    # bi = data.loc[:, 'bi':]
    # for i in Basis['Basis']:
    


if __name__ == '__main__':
    Data = pd.read_csv("simplex/table1.csv")
    simplex(Data)