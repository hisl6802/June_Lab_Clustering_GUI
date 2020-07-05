#Creating a class containing functions that will be used in GUI
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering
import sklearn.preprocessing as pp
import statistics as stat
import GuiBackground as GB
from tkinter import filedialog


class GUIUtils:

    def dataIntegrity(file):
        #Read in Volcano Plot data
        volcano = pd.read_excel(file)
        #grab the first row the volcano data
        check = volcano['Unnamed: 0']

        #determine the shape of the array
        checkShape = check.shape[0]

        #create array that can save the fixed data and the data that did not need to be fixed
        correctedArray = np.zeros(checkShape)

        #search each of the volcano data rows to determine if they have double decimals.
        for i in range(check.shape[0]):
            #grab the row corresponding to the current run through the loop
            curVal = check[i]

            #reset the number of decimals to 0 before checking the string for decimal points
            decimal = 0

            #creating a string that will contain the corrected string
            corrected = ''

            #Determine if the value is a float to allow for determination of whether or not we need to check it for the appropriate value
            if isinstance(curVal,float) != True:
                #Look through the strings to find data integrity issues. 
                for j in range(len(curVal)):
                    #Check for decimals otherwise add the value to a string
                    value = curVal[j]
                    if value == '.':
                        decimal += 1
                        if decimal == 1:
                            corrected += value
                    else:
                        corrected += value
                        if j == len(curVal)-1:
                            try:
                                correctedArray[i] = float(corrected)
                            except CorrectionError:
                                print('Error in correcting the data integrity issue')
            else:
                #save the data that did not need to be corrected to the correctedArray
                correctedArray[i] = curVal

        #Replace the values in the dataframe with the appropriate values
        volcano['Unnamed: 0'] = correctedArray

        #specify the file to write to
        output = pd.ExcelWriter('/Users/bradyhislop/Desktop/testing1.xlsx')

        #write to excel file
        volcano.to_excel(output,index=False)

        #save the excel sheet
        output.save()

    def createClustergram():
        #ask the user to select the file that they would like to create a clustergram for.
        file = filedialog.askopenfilename()
        #Open the excel file that the user to looking to use for their clustering analysis
        metab_data = pd.read_excel(file, sheet_name='Medians')

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
            data[i,:] = GB.standardize(data[i,:])

        #create dendrogram and plot data
        GB.create_dendrogram(data)
        GB.plotting()

    def groupMedians(file):
        #read in the file containing all of the metabolite values
        #file = '/Users/bradyhislop/Box/ClusteringGUI/Examples/Metaboanalyst-Data-Input.xlsx'
        medians = pd.read_excel(file)

        #get the group letters to know which groups to find the medians of
        groups = medians['mz']

        #determine the number of groups and then create a list or array of the appropriate
        #beginning and ending of each group.
        #This assumes that the groups are all of equal size which should be
        #the goal for any and all analysis. Groups with out the same sizes should be considered
        #inappropriate for analysis in this context, additionally it should be noted that statistics
        #with out the same groups sizes can lead to incorrect analysis. 
        num_groups = int(medians['Unnamed: 0'][23][0])
        factor = len(medians['Unnamed: 0'])/num_groups


        #create a numpy array containing 7 columns to allow for input of the m/z values and the groups
        mediansOut = np.zeros((medians.shape[1]-2,num_groups+1))
            

        #populate the first column of the array with the m/z values
        mediansOut[:,0] = medians.columns[2:medians.shape[1]]


        #Get the medians for each group and metabolite
        for i in range(num_groups):
            #calculate the start and end for each set of median calculations
            start = int(factor*i)
            end = int((factor*(i+1)))
            for j in range(mediansOut.shape[0]):
                #find the median for the first groups of values
                curMean = stat.mean(medians[medians.columns[j+2]][start:end])
                #put medians into the appropriate table
                mediansOut[j,i+1] = curMean

        #create list contains the headers for the files
        medianList = ['m/z']
        for i in range(num_groups):
            medianList.append('M' +str(i+1))

        #create dictionary that contains the data with there appropriate headers to input to a dataframe and
        #then be saved to a csv file
        medianDict = {}
        for i in range(num_groups+1):
            #input the appropriate data and key to the dictionary
            medianDict[medianList[i]] = mediansOut[:,i]

        #create dataframe that prepares the data to be input to a csv file
        mediansCSV = pd.DataFrame(data=medianDict)

        #specify the file that I want the program to write to.
        mediansCSV.to_csv('/Users/bradyhislop/Desktop/Medians.csv',columns=medianList,index =False)



    def linkageComparison(file,num_comps):
        #This function creates multiple comparisons of linkages 
        # to determine the best linkage function

        #Need to figure out how to either give the user the ability to pick which linkage functions to compare
        # or give them all four of the linkage functions.

        #Open the excel file that the user to looking to use for their clustering analysis
        metab_data = pd.read_excel(file, sheet_name='Medians')

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
            data[i,:] = GB.standardize(data[i,:])

        if num_comps == 2:
            #Create the linkage matrix
            linkageOne = linkage(data,'ward')
            linkageTwo = linkage(data,'single')

            #Create the appropriate plt figure to allow for the comparison of linkage functions
            fig, axes = plt.subplots(1,2,figsize=(10,8))

            #create the dendrograms
            dend1 = dendrogram(linkageOne,ax=axes[0],above_threshold_color='y',orientation='left')
            dend2 = dendrogram(linkageTwo,ax=axes[1],above_threshold_color='y',orientation='left')

            #create the plot
            plt.show()

        elif num_comps == 3:
            #Create the linkage matrix
            linkageOne = linkage(data,'ward')
            linkageTwo = linkage(data,'single')
            linkageThree = linkage(data,'complete')

            #Create the appropriate plt figure to allow for the comparison of linkage functions
            fig, axes = plt.subplots(1,3,figsize=(10,8))

            #create the dendrograms
            dend1 = dendrogram(linkageOne,ax=axes[0],above_threshold_color='y',orientation='left')
            dend2 = dendrogram(linkageTwo,ax=axes[1],above_threshold_color='y',orientation='left')
            dend3 = dendrogram(linkageThree,ax=axes[2],above_threshold_color='y',orientation='left')

            #create the plot
            plt.show()

        elif num_comps == 4:
            #Create the linkage matrix
            linkageOne = linkage(data,'ward')
            linkageTwo = linkage(data,'single')
            linkageThree = linkage(data,'complete')
            linkageFour = linkage(data, 'average')

            #Create the appropriate figure to allow for the comparison of linkage functions
            fig, axes = plt.subplots(2,2,figsize=(10,8))

            #create the dendrograms
            dend1 = dendrogram(linkageOne,ax=axes[0],above_threshold_color='y',orientation='left')
            dend2 = dendrogram(linkageTwo,ax=axes[1],above_threshold_color='y',orientation='left')
            dend3 = dendrogram(linkageThree,ax=axes[2],above_threshold_color='y',orientation='left')
            dend4 = dendrogram(linkageFour,ax=axes[3],above_threshold_color='y',orientation='left')

            #Create the plot
            plt.show()

