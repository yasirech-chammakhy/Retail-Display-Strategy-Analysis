import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from MDLP import MDLP_Discretizer
import pandas as pd


def main():

    ######### USE-CASE EXAMPLE #############

    #read dataset
    #dataset = datasets.load_iris()
    df = pd.read_csv('new_Base_CDM_balanced_V2.csv', sep=';',header=0)    

    #X, y = dataset['data'], dataset['target']
    X , y = df.iloc[:,[1,2,3,4,6]].values , df.iloc[:,0].values
    print(y)
    #feature_names, class_names = dataset['feature_names'], dataset['target_names']
    feature_names, class_names = df.columns[1:5] , df.columns[0]
    
    numeric_features = np.arange(X.shape[1])  # all fetures in this dataset are numeric. These will be discretized

    #Split between training and test
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    #Initialize discretizer object and fit to training data
    discretizer = MDLP_Discretizer(features=numeric_features)
    #discretizer.fit(X_train, y_train)
    #X_train_discretized = discretizer.transform(X_train)
    X_discretized = discretizer.fit_transform(X,y)
    import json
    dict = discretizer._cuts
    values = dict.values()
    
    with open('cut.txt', 'w') as f:
        for _list in values:
            f.write(str(_list) + '\n')

    #apply same discretization to test set
    #X_test_discretized = discretizer.transform(X_test)

    ######################################################################################################################
    # #Print a slice of original and discretized data
    # print 'Original dataset:\n%s' % str(X[0:5])
    # print 'Discretized dataset:\n%s' % str(X_discretized[0:5])

    # #see how feature 0 was discretized
    # print 'Feature: %s' % feature_names[1]
    
    # print 'Interval cut-points: %s' % str(discretizer._cuts[1])
    
    # print 'Bin descriptions: %s' % str(discretizer._bin_descriptions[1])
    
    ######################################################################################################################
    pd.DataFrame(X_discretized,columns=["x1","x2","x3","x4","x6"]).to_csv("./discretized_data.csv")
    ######################################################################################################################
    # #Print a slice of original and discretized data
    # print 'Original dataset:\n%s' % str(X_train[0:5])
    # print 'Discretized dataset:\n%s' % str(X_train_discretized[0:5])

    # #see how feature 0 was discretized
    # print 'Feature: %s' % feature_names[0]
    # print 'Interval cut-points: %s' % str(discretizer._cuts[0])
    # print 'Bin descriptions: %s' % str(discretizer._bin_descriptions[0])

if __name__ == '__main__':
    main()