import numpy as np
import cv2 as cv2
import os
import tkinter
import csv
from tkinter import *
from tkinter import messagebox
from Image import Image
from Feature import Feature
from Label import Label
from SVM import SVM
from LibSvm import LibSvm

class Main:

    def main():

        image = Image()
        feature = Feature()
        label = Label()
        svm = SVM()
        libSvm = LibSvm()

        #GUI
        root = tkinter.Tk()
        root.geometry("500x450")
        root.title("Passion Fruit Disease Identification")

        #function for load images from folder
        def gettingImages(path):
            imagesName =[]
            for root, dirs, files in os.walk(path):
                for filename in files:
                    imagesName.append(filename)
            return imagesName

        #function for pass images to image preprocessing
        def preprocess():
            folderPath = "../Images/Images_Original/"
            count = -1

            #getting all images from original folder
            imagesName = gettingImages(folderPath)

            for imageName in imagesName:
                count = count + 1
                image.ImagePreprocessing(img_name=imageName)
                if len(imagesName) - 1 == count:
                    messagebox.showinfo("", "Successfully preprocessed")

        # function for pass images to image preprocessing
        def segment():

            folderPath = "../Images/Images_Preprocessed/"
            count = -1

            ImagesName = gettingImages(folderPath)

            for imageName in ImagesName:
                count = count + 1
                image.ImageSegmentation(img_name=imageName)
                if len(ImagesName) - 1 == count:
                    messagebox.showinfo("Success", "Successfully Segmented")

        # adding labels to csv files
        def ladelAdding():
            label.allocateLabel()

        # creating label adding file
        def creatingLabelFile():
            label.createLabelFile()

        def featureExtract():

            #lists for store features vector values
            lab_features_list = []
            hsv_features_list = []
            gray_features_list = []
            original_features_list = []

            startIndex = 0
            endIndex = 0
            arrayLength = 0
            count = 0
            folderPathIndex = 0 # identify the folder path
            csvFilePathIndex = [] # identify csv file path
            success = 2
            index = 1

            # get all images folder paths to feature extraction
            # foldersPath = ["../Images/Segmented_Images/Original/",
            #               "../Images/Segmented_Images/Lab/",
            #               "../Images/Segmented_Images/HSV/",
            #               "../Images/Segmented_Images/Gray/"]

            foldersPath = ["../Images/Segmented_Images/Lab/",
                           "../Images/Segmented_Images/HSV/",
                           "../Images/Segmented_Images/Gray/",
                           "../Images/Segmented_Images/Original/"]

            for folderPath in foldersPath:
                if folderPath == "../Images/Segmented_Images/Lab/":
                    folderPathIndex = 1
                if folderPath == "../Images/Segmented_Images/HSV/":
                    folderPathIndex = 2
                if folderPath == "../Images/Segmented_Images/Gray/":
                    folderPathIndex = 3
                if folderPath == "../Images/Segmented_Images/Original/":
                     folderPathIndex = 4

                imagesName = gettingImages(folderPath)
                for imageName in imagesName:
                    print("Image name: "+imageName+" was feature extracted ("+ str(index) +")")
                    count = count + 1
                    count1 = 0
                    index += 1

                    feature_array = feature.FeatureExtraction(img_name=imageName, img_path=folderPath)

                    arrayLength = len(feature_array)*count
                    endIndex = arrayLength - 1
                    startIndex = endIndex - 256
                    # print("startIndex = "+str(startIndex)+", endIndex = "+str(endIndex)+", arrayLength = "+str(arrayLength))

                    for i in range(startIndex, endIndex+1):
                        if count1 == 257*count:
                            count1 = 0
                        # print(str(i) + " = " + str(feature_array[count1]))
                        if folderPathIndex == 1:
                            lab_features_list.insert(i, feature_array[count1])
                            csvFilePathIndex.insert(0, 1)
                        if folderPathIndex == 2:
                            hsv_features_list.insert(i, feature_array[count1])
                            csvFilePathIndex.insert(1, 2)
                        if folderPathIndex == 3:
                            gray_features_list.insert(i, feature_array[count1])
                            csvFilePathIndex.insert(2, 3)
                        if folderPathIndex == 4:
                            original_features_list.insert(i, feature_array[count1])
                            csvFilePathIndex.insert(3, 4)
                        count1 = count1 + 1
                    #messagebox.showinfo("Success", "Successfully features were extracted")

            # pass the lab feature list to create multidimensional list with titles
            success = feature.CreateFeaturesMultiDimentionList(lab_features_list, folderPath= csvFilePathIndex[0])
            feature.csvFileCreationNotificationMessage(successIndex=success, category=csvFilePathIndex[0])

            # pass the hsv feature list to create multidimensional list with titles
            success = feature.CreateFeaturesMultiDimentionList(hsv_features_list, folderPath= csvFilePathIndex[1])
            feature.csvFileCreationNotificationMessage(successIndex=success, category=csvFilePathIndex[1])

            # pass the gray feature list to create multidimensional list with titles
            success = feature.CreateFeaturesMultiDimentionList(gray_features_list, folderPath= csvFilePathIndex[2])
            feature.csvFileCreationNotificationMessage(successIndex=success, category=csvFilePathIndex[2])

            # pass the original images features list to create multidimensional list with titles
            success = feature.CreateFeaturesMultiDimentionList(original_features_list, folderPath=csvFilePathIndex[3])
            feature.csvFileCreationNotificationMessage(successIndex=success, category=csvFilePathIndex[3])

            #print(len(lab_features_list))

        # for basic purposes
        def rename():
            image.RenameImage()

        def rotate():
            image.RotateImages()

        def trainModel():
            activity = 'train'
            svm.createModel()

        def testModel():
            activity = 'test'
            aCount = 0
            bCount = 0
            cCount = 0

            for i in range(0,1000):
                label = svm.testModel()
               # print(label)
                if label == 'A':
                    aCount += 1
                if label == 'B':
                    bCount += 1
                if label == 'C':
                    cCount += 1

            if (aCount >= bCount) and (aCount >= cCount):
                print("Non disease")
                messagebox.showinfo("Success", "Non-disease")
            elif (bCount >= aCount) and (bCount >= cCount):
                print("Scab disease")
                messagebox.showinfo("Success", "Scab disease")
            else:
                print("Woodiness disease")
                messagebox.showinfo("Success", "Woodiness disease")


        preprocess_btn = Button(text="Preprocessing", command = preprocess)
        preprocess_btn.place(x=10,y=10)

        rotate_btn = Button(text="Rotate Image", command=rotate)
        rotate_btn.place(x=250, y=10)

        segment_btn = Button(text="Segmentation", command = segment)
        segment_btn.place(x=10, y=50)

        rename_btn = Button(text="Rename Image", command=rename)
        rename_btn.place(x=250, y=50)

        segment_btn = Button(text="Feature Extraction", command=featureExtract)
        segment_btn.place(x=10, y=90)

        crt_label_btn = Button(text="Creating Label File", command=creatingLabelFile)
        crt_label_btn.place(x=10, y=130)

        label_adding_btn = Button(text="Adding Label", command=ladelAdding)
        label_adding_btn.place(x=10, y=170)

        test_btn = Button(text="Train", command=trainModel)
        test_btn.place(x=10, y=250)

        test_btn1 = Button(text="Test", command=testModel)
        test_btn1.place(x=100, y=250)

        root.mainloop()



    if __name__ == '__main__':
        main()


