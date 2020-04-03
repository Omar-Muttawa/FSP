import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

def getdata():
    px = pd.read_csv("PriceData.csv")
    return px

def main():
    px = getdata()
    print(px)
    logpx = np.log(px)
    logpx.plot()

if __name__ == '__main__':
    main()
