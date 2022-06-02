from pprint import pprint
import numpy as np



def swap(a, b):
    return b, a


def split(data):
    print(data)
    return data[:, :4], data[:, 4]

def fillF(data, cj, cb):
    f = []
    for i in range(data.shape[1]):
        f+=(cb[i]*data[4][i])
    return f


def delta(data, cj, cb, a0):
    f = []
    print(a0)
    for j in range(data.shape[1]):
        d = 0
        for i in range(data.shape[0]):
            d+=cb[i]*a0[i]
        f.append(d-cj[j])
    return f


def findCol(f):
    return(np.array(f).argmin())


def findRow(a0, data, J):
    a0 = a0.transpose()/data[:,J]
    a0 = np.where(a0 >= 0, a0, np.inf)
    a0 = a0.argmin()
    return a0


def newMatrix(J,I, data, a0):
    row = data[I] / data[I][J]
    element = data[I][J]
    column = data[:, J] * (-1 / element)
    data[I] = row
    data[:, J] = column
    data[I][J] = element
    a0[J] = a0[J]/element
    return data, a0


def rectangle(data1, data2, r, s):
    for i in range(data1.shape[0]):
        for j in range(data1.shape[1]):
            if i != r and j != s:
                data2[i][j] = (data1[i][j]*data1[r][s] - data1[r][j] * data1[i][s])/data1[r][s]
    return data2


def simplex(data, cj, a0, cb):
    Q = 0
    f = delta(data, cj, cb, a0)
    pprint(f)
    J = findCol(f)
    I = findRow(a0, data, J)
    cb[I], cj[J] = swap(cb[I], cj[J])
    print(cb, cj)
    new_data, new_a0 = newMatrix(J,I,data, a0)
    new_a0 = new_a0.reshape(1,6)
    a0 = a0.reshape(1,6)
    old_data = np.concatenate((data, a0.T), axis=1)
    new_data = np.concatenate((new_data, new_a0.T), axis=1)
    data = rectangle(old_data, new_data, I, J)
    data, a0 = split(data)
    f = delta(data, cj, cb, a0)
    if any(d < 0 for d in f):
        simplex(data, cj, a0, cb)
    a0 = a0.reshape(1,6)
    print(a0)
    print(cb)
    print(80*80)
    return np.concatenate((data, a0.T), axis=1)
    




if __name__ == '__main__':
    Data = np.array([
        [1000, 700, 500, 1100],
        [30, 20, 20, 35],
        [1,  0,  0,  0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    print(Data.shape)
    Cj = np.array([70, 80, 60 , 80])
    A0 = np.array([180000, 5000, 100, 80, 100 ,60])
    cb = [0,0,0,0,0,0]
    print(simplex(Data, Cj, A0, cb))
