import numpy as np
import statistics as stat
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from matplotlib import pyplot as plt
import pandas as pd


        
    #Standardizing the data that is input to python.
def standardize(data):
    #I would like to add the ability to check for the number of rows or columns that are given in a numpy array.
    #find the mean and standard deviation of the given row(eventually will need to move this to allow for the entire table to input.)
    mean_data = stat.mean(data)
    std_data = stat.stdev(data)
    dataCur = np.zeros(data.shape[0])

    for i in range(data.shape[0]):
        dataCur[i] = (data[i]-mean_data)/std_data

    return dataCur

#creating function that creates the dendrogram
def create_dendrogram(data, **kwargs):
    #Create the linkage matrix
    linkageOut = linkage(data,'ward')
    #create the dendrogram
    dendrogram(linkageOut)

#initialize the plot
def plotting():
    #create a figure window
    plt.title('Medians Clustering')
    plt.xlabel('Clustered Metabolites')
    plt.show()

    