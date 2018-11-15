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

        def test():
            svm.test()

        def test1():
            libSvm.CreateModel()


        # gray data set train and test functions
        def trainGrayData1():
            print()

        def trainGrayData2():
            print()

        def trainGrayData3():
            print()

        # HSV data set train and test functions
        def trainHsvData1():
            print()

        def trainHsvData2():
            print()

        def trainHsvData3():
            print()

        # Lab data set train and test functions
        def trainLabData1():
            print()

        def trainLabData2():
            print()

        def trainLabData3():
            print()

        # Original dataset train and test functions
        def trainOriginalData1():
            print()

        def trainOriginalData2():
            print()

        def trainOriginalData3():
            print()


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

        test_btn = Button(text="test", command=test)
        test_btn.place(x=10, y=210)

        test_btn1 = Button(text="Multiclass", command=test1)
        test_btn1.place(x=100, y=210)

        # Gray data set train and test buttons
        train_gray_btn = Button(text="Gray-Train & Test 1", command=trainGrayData1)
        train_gray_btn.place(x=10, y=250)

        train_gray_btn = Button(text="Gray-Train & Test 2", command=trainGrayData2)
        train_gray_btn.place(x=150, y=250)

        train_gray_btn = Button(text="Gray-Train & Test 3", command=trainGrayData3)
        train_gray_btn.place(x=290, y=250)

        # HSV data set train and test buttons
        train_hsv_btn = Button(text="HSV-Train & Test 1", command=trainHsvData1)
        train_hsv_btn.place(x=10, y=290)

        train_hsv_btn = Button(text="HSV-Train & Test 2", command=trainHsvData2)
        train_hsv_btn.place(x=150, y=290)

        train_hsv_btn = Button(text="HSV-Train & Test 3", command=trainHsvData3)
        train_hsv_btn.place(x=290, y=290)

        # Lab data set train and test buttons
        train_lab_btn = Button(text="Lab-Train & Test 1", command=trainLabData1)
        train_lab_btn.place(x=10, y=330)

        train_lab_btn = Button(text="Lab-Train & Test 2", command=trainLabData2)
        train_lab_btn.place(x=150, y=330)

        train_lab_btn = Button(text="Lab-Train & Test 3", command=trainLabData3)
        train_lab_btn.place(x=290, y=330)

        # Original data set train and test buttons
        train_original_btn = Button(text="Original-Train & Test 1", command=trainOriginalData1)
        train_original_btn.place(x=10, y=370)

        train_original_btn = Button(text="Original-Train & Test 2", command=trainOriginalData2)
        train_original_btn.place(x=150, y=370)

        train_original_btn = Button(text="Original-Train & Test 3", command=trainOriginalData3)
        train_original_btn.place(x=290, y=370)

        root.mainloop()



    if __name__ == '__main__':
        main()


