import numpy as np
import timers
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
import csv
import pickle
from tkinter import messagebox
import os

class SVM(object):

    def createModel(self):

        path = "../Features/Lab_features.csv"
        attributesArray = []
        featuresArray = []
        labelsArray = []
        fullDataArray = []
        shuffeledFullDataArray = []
        index = 0

        with open(path) as labels:
            labelList = csv.reader(labels)
            for labelRow in labelList:
                fullDataArray.insert(index, labelRow)
                index += 1

        arr = np.arange(0,len(fullDataArray))
        np.random.shuffle(arr)
        #print(len(arr))
        count = 0

        print("Result....")

        for n in range(0, len(fullDataArray)+1):
            if n != 0 and count < len(fullDataArray):
                index = arr[count]
                if index == 0:
                    shuffeledFullDataArray.insert(0, fullDataArray[0])
                    count += 1
                else:
                    shuffeledFullDataArray.insert(n, fullDataArray[index])
                    count += 1

        # make feature array
        for i in range(0, len(shuffeledFullDataArray)-1):
            row = []
            #featuresArray.append([]) # remove this, because occur error
            for x in range(0,256):
                row.insert(x, shuffeledFullDataArray[i+1][x+1])
            featuresArray.insert(i,row)

        # make attributes array
        for i in range(0,256):
            attributesArray.insert(i, shuffeledFullDataArray[0][i+1])

        # make labels array
        for i in range(0, len(shuffeledFullDataArray)-1):
            labelsArray.insert(i, shuffeledFullDataArray[i+1][257])

        # for actual features
        # X_train = featuresArray[0:3343]
        # X_test = featuresArray[3343:]
        # y_train = labelsArray[0:3343]
        # y_test = labelsArray[3343:]

        # dataset 1
        X_train = featuresArray[0:244]
        X_test = featuresArray[244:]
        y_train = labelsArray[0:244]
        y_test = labelsArray[244:]

        # dataset 2
        # X_train = featuresArray[0:484]
        # X_test = featuresArray[484:]
        # y_train = labelsArray[0:484]
        # y_test = labelsArray[484:]

        # dataset 3
        # X_train = featuresArray[0:720]
        # X_test = featuresArray[720:]
        # y_train = labelsArray[0:720]
        # y_test = labelsArray[720:]

        # dataset 4
        # X_train = featuresArray[0:958]
        # X_test = featuresArray[958:]
        # y_train = labelsArray[0:958]
        # y_test = labelsArray[958:]

        # dataset 5
        # X_train = featuresArray[0:1200]
        # X_test = featuresArray[1200:]
        # y_train = labelsArray[0:1200]
        # y_test = labelsArray[1200:]

        # Split dataset into training set and test set
        #X_train, X_test, y_train, y_test = train_test_split(featuresArray, labelsArray, test_size=0.3, random_state=109)  # 70% training and 30% test

        # Create a svm Classifier
        #clf = SVC(kernel='linear')
        clf = SVC(kernel='poly',gamma='auto')  # Linear or poly

        #clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state = 0) #random forest
        #clf = SVC(kernel='linear', gamma='auto')  # Linear or poly

        try:
            # Train the model using the training sets
            clf.fit(X_train, y_train)

            # save the model to disk
            filename = '../Model/Train/finalized_model.sav'
            pickle.dump(clf, open(filename, 'wb'))
            messagebox.showinfo("Success", "Successfully created model!")
        except:
            messagebox.showerror("Fail", "Error occured!")

        # for testing model
        # newModel = pickle.load(open("../Model/finalized_model.sav", "r"))

        try:
            # Predict the response for test dataset
            y_pred = clf.predict(X_test)

            # Model Accuracy: how often is the classifier correct?
            accuracy = metrics.accuracy_score(y_test, y_pred) * 100
            messagebox.showinfo("Success", "Accurancy of this model: " + str(round(accuracy, 2)) + "%")

            print("Accuracy: " + str(round(accuracy, 2)) + "%")
            print(confusion_matrix(y_test, y_pred))
            print(classification_report(y_test, y_pred))
            print("-------------------------------------------------------")

            f = open("../Model/Train/accuracy.txt", "w+")
            f.write("Accuracy of model = %f" % round(accuracy, 2) + "%")
            f.close()

        except:
            messagebox.showerror("Fail", "Error occured with testing!")

    def testModel(self):
        path = "../Features/Lab_features.csv"
        attributesArray = []
        featuresArray = []
        labelsArray = []
        fullDataArray = []
        shuffeledFullDataArray = []
        index = 0

        with open(path) as labels:
            labelList = csv.reader(labels)
            for labelRow in labelList:
                fullDataArray.insert(index, labelRow)
                index += 1

        arr = np.arange(0, len(fullDataArray))
        np.random.shuffle(arr)
        # print(len(arr))
        count = 0

        for n in range(0, len(fullDataArray) + 1):
            if n != 0 and count < len(fullDataArray):
                index = arr[count]
                if index == 0:
                    shuffeledFullDataArray.insert(0, fullDataArray[0])
                    count += 1
                else:
                    shuffeledFullDataArray.insert(n, fullDataArray[index])
                    count += 1

        # make feature array
        for i in range(0, len(shuffeledFullDataArray) - 1):
            row = []
            # featuresArray.append([]) # remove this, because occur error
            for x in range(0, 256):
                row.insert(x, shuffeledFullDataArray[i + 1][x + 1])
            featuresArray.insert(i, row)

        # make attributes array
        for i in range(0, 256):
            attributesArray.insert(i, shuffeledFullDataArray[0][i + 1])

        # make labels array
        for i in range(0, len(shuffeledFullDataArray) - 1):
            labelsArray.insert(i, shuffeledFullDataArray[i + 1][257])

        featureArray = [] # new array for put one array elements

        #try:
        featureArray.insert(0, featuresArray[0])
        X_test = featureArray

        # load the model from disk
        filename = "../Model/Test/finalized_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))

        # Predict the response for test dataset
        y_pred = loaded_model.predict(X_test)
        return y_pred[0]

        # except:
        #     messagebox.showerror("Fail", "Error occured!")
