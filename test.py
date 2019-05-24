import numpy as np

if __name__ == '__main__':
    d = 1
    for i in range(100):
        T = 10 / (np.log(i + d))
        print(T)