import numpy as np
import cv2 as cv2
import os
import tkinter
import csv
from tkinter import messagebox

class Label(object):

    # get images
    def getImagesNames(self):
        imagesName = []
        folderPath = "../Images/Images_Original/"
        for root, dirs, files in os.walk(folderPath):
            # make array using img names ex: img_1, img_2
            for filename in files:
                imagesName.append(filename.split('.',1)[0])
        #print(imagesName)
        return imagesName

    # show success or failure alert
    def successOrFail(self, value, type):
        successMessage = value
        type = type

        # success of failure on creating label adding csv file
        if type == 1:
            if successMessage == 1:
                messagebox.showinfo("Success", "Successfully created label adding file!")
            if successMessage == 0:
                messagebox.showerror("Fail", "Error occured!")

        if type == 2:
            if successMessage == 1:
                messagebox.showinfo("Success", "Successfully added labels!")
            if successMessage == 0:
                messagebox.showerror("Fail", "Error occured!")

    # creating label adding file
    def createLabelFile(self):
        successMessage = 1
        csvFilePath = '../Label/Label_file.csv'
        imagesName = Label.getImagesNames(self)

        try:
            with open(csvFilePath, mode='w', newline='') as label_file:
                label_writer = csv.writer(label_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                label_writer.writerow(['Name', 'Label'])
                for i in imagesName:
                    # print(i)
                    label_writer.writerow(i.split())
                successMessage = 1
        except:
            successMessage = 0

        Label.successOrFail(self, value=successMessage, type=1)


    # add labels to csv files
    def allocateLabel(self):

        successMessage = 1
        path = ''

        pathArray = ["../Features/Lab_features.csv",
                     "../Features/HSV_features.csv",
                     "../Features/Gray_features.csv",
                     "../Features/Original_images_features.csv"
                     ]

        for x in range(0,len(pathArray)):

            featuresArray = []  # all feature csv file data are inserted into array
            index = 0
            count1 = 1
            path = pathArray[x]

            try:
                # get all feature values to featureArray
                with open(path) as feature:
                    featureList = csv.reader(feature)
                    for featureRow in featureList:
                        featuresArray.insert(index, featureRow)
                        index = index + 1

                # print(featuresArray[0][257])

                # add label from label.csv
                for x in range(0, len(featuresArray) - 1):
                    imgName = '_'.join(featuresArray[count1][0].split('_', 2)[:2])
                    # print(imgName)
                    with open("../Label/Label_file.csv") as label:
                        labelList = csv.reader(label)
                        for labelRow in labelList:
                            if labelRow[0] == imgName:
                                featuresArray[count1][257] = labelRow[1]
                    count1 += 1

                # new labeled features save in the csv file

                with open(path, mode='w', newline='') as feature_file:
                    feature_writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                    for i in featuresArray:
                        # print(i)
                        feature_writer.writerow(i)
                successMessage = 1
            except:
                successMessage = 0

        Label.successOrFail(self, value=successMessage, type=2)