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

class Main:

    def main():

        image = Image()
        feature = Feature()
        label = Label()

        #GUI
        root = tkinter.Tk()
        root.geometry("400x200")
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

        #tset
        def test():
            label.allocateLabel()



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
                    count = count + 1
                    count1 = 0

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


        preprocess_btn = Button(text="Preprocessing", command = preprocess)
        preprocess_btn.place(x=10,y=10)

        segment_btn = Button(text="Segmentation", command = segment)
        segment_btn.place(x=10, y=50)

        segment_btn = Button(text="Feature Extraction", command=featureExtract)
        segment_btn.place(x=10, y=90)

        test_btn = Button(text="Test", command=test)
        test_btn.place(x=10, y=140)
        root.mainloop()



    if __name__ == '__main__':
        main()


