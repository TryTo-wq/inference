import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from sklearn.preprocessing import scale,normalize

def heat(data_origin, threshold, label, save_path):
    data = []
    for i in data_origin:
        tmp = []
        for j in data_origin:
            t = (j-i)/j
            if t>threshold :
                tmp.append(1)
            elif t<-threshold:
                tmp.append(-1)
            else:
                tmp.append(0)
        data.append(tmp)
    data =np.array(data)
    print(data)
    border = len(data_origin)
    border_len = 2
    plt.figure()
    plt.plot([0,0],[0,border],linewidth=border_len-0.5,color='black')
    plt.plot([0,border],[0,0],linewidth=border_len-0.5,color='black')
    plt.plot([border,border],[0,border],linewidth=border_len,color='black')
    plt.plot([0,border],[border,border],linewidth=border_len,color='black')
    ax = sns.heatmap(data,cbar = False,cmap = ["white","grey","black"],square = True,linewidth = 0.005,center = 0)
    ax.set_yticklabels(label)
    ax.set_xticklabels(label)
    plt.savefig(save_path,transparent = True,pad_inches = 0,bbox_inches = 'tight')

label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
#data_origin = [0.5021,0.6362,0.7885,0.8965,0.7467,0.75,0.93,0.78,0.81,0.75,0.68,0.78,0.71,0.95]
#data_origin = [0.68,0.21,0.78,0.86,0.86,0.78,0.82,0.80,0.86,0.79,0.70,0.51,0.50,0.87]
data_origin = [0.1,0.40,0.68,0.79,0.87,0.39,0.61,0.86,0.80,0.76,0.71,0.26,0.47,0.86]
heat(data_origin, 0.05,label, "heatmap3.pdf")