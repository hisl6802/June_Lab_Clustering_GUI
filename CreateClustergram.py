import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import sklearn.preprocessing as pp
import statistics as stat

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

#creating function that 
def create_dendogram(data, **kwargs):
    #Create the linkage matrix
    linkageOut = linkage(data,'ward')
    #create the dendrogram
    dendrogram(linkageOut)

def plotting():
    #create a figure window
    #fig = plt.figure(figsize=(25,10))
    plt.title('Jake Medians Clustering')
    plt.xlabel('Clustered Metabolites')
    plt.show()

#Open the excel file that the user to looking to use for their clustering analysis
metab_data = pd.read_excel(r'/Users/bradyhislop/Box/ClusteringGUI_python/Jake_Medians.xlsx',sheet_name='Medians')

#finding the number of groups in the metabolomics study to allow for proper clustering of the results
num_groups = metab_data.shape[1] - 2

#creating a numpy array that is the size of the data that is being read in.
data = np.zeros((metab_data.shape[0],metab_data.shape[1]-2))

for i in range(num_groups):
    #create the appropriate string to add to the group name
    num = str(i + 1)
    g_name = "M" + num
    #grab the Medians for each group
    medianCur = metab_data[g_name]
    #add the medians data to the array to be clustered
    data[:,i] = medianCur
    
#Standardize the data before clustering the results
for i in range(metab_data.shape[0]):
    data[i,:] = standardize(data[i,:])

#clusteringOutput = AgglomerativeClustering(distance_threshold=0, n_clusters=None).fit(data)
create_dendogram(data)
plotting()



