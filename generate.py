from numpy import nan
import xlrd
import os
import pathlib
import re
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
# for f in files:
# 	print(f)
file ="bq-results-20210503-215650-czuk60m7egnp.csv"
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)
plt.close("all")

def test_read(fileCsv):
    df = pd.read_csv(fileCsv)
    
    df[['X', 'Y', 'Z']] = df['position'].str.replace("(","").replace(")","").str.split(',', 2, expand=True)
    
    df[['X']] = df[['X']].apply(pd.to_numeric) 
    df[['Y']] = df[['Y']].apply(pd.to_numeric)
    print(df)
    
    level = 1
    
    for x in range(1, 9):
        level = x
        chart = df[df.level.eq(level)]
        # generate 2 2d grids for the x & y bounds
        # x, y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-30, 30, 100))       
        plot = chart.plot.scatter(x="X", y="Y", s = 0.01)    
        plot.set_title(f"level {level}")
    
    plt.tight_layout()
    plt.show()
    return

def main():    
    path = pathlib.Path().absolute()
    files = os.listdir(path)
    # rename file so it look nice
    for f in files:
        if not f.endswith(".csv"):
            continue
        test_read(f)

    files = os.listdir(path)


main()