import cv2 as cv2
import numpy as np
import matplotlib as plt
import csv
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image

class Feature(object):
    
    def get_pixel(img, center, x, y):
        new_value = 0
        try:
            if img[x][y] >= center:
                new_value = 1
        except:
            pass
        return new_value
    
    def lbp_calculated_pixel(img, x, y):
        '''

             64 | 128 |   1
            ----------------
             32 |   0 |   2
            ----------------
             16 |   8 |   4

            '''
        center = img[x][y]
        val_ar = []
        val_ar.append(Feature.get_pixel(img, center, x - 1, y + 1))  # top_right
        val_ar.append(Feature.get_pixel(img, center, x, y + 1))  # right
        val_ar.append(Feature.get_pixel(img, center, x + 1, y + 1))  # bottom_right
        val_ar.append(Feature.get_pixel(img, center, x + 1, y))  # bottom
        val_ar.append(Feature.get_pixel(img, center, x + 1, y - 1))  # bottom_left
        val_ar.append(Feature.get_pixel(img, center, x, y - 1))  # left
        val_ar.append(Feature.get_pixel(img, center, x - 1, y - 1))  # top_left
        val_ar.append(Feature.get_pixel(img, center, x - 1, y))  # top

        power_val = [1, 2, 4, 8, 16, 32, 64, 128]
        val = 0
        for i in range(len(val_ar)):
            val += val_ar[i] * power_val[i]
            # print(val)
        return val
    
    def FeatureExtraction(self, img_name, img_path):
        img = img_name
        path = img_path
        image_file = path + img
        image = cv2.imread(image_file)
        #img_resize = cv2.resize(img_bgr, (400, 600))
        height, width, channel = image.shape
        # img_hsv = cv2.cvtColor(img_resize, cv2.COLOR_BGR2Lab)
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_lbp = np.zeros((height, width, 3), np.uint8)
        for i in range(0, height):
            for j in range(0, width):
                img_lbp[i, j] = Feature.lbp_calculated_pixel(img_gray, i, j)
                # print(img_lbp[i,j])
        hist_lbp = cv2.calcHist([img_lbp], [0], None, [256], [0, 256])

        image_feature_array = []
        image_feature_array.insert(0,img.split('.')[0]) # add image name for feature array
        for i in range(1,257):
            image_feature_array.insert(i,hist_lbp[i-1][0])
        print("Happening...")
        return image_feature_array # image name + 256 textures

    def test1(self):
        #img = 'img_1_2_3.jpg'
        #x = '_'.join(img.split('_',2)[:2])
        #x = img.split('.')[0]

        preImagesName = []
        newImagesName = []
        index = 0
        directory = '../Images/Rename_images/'

        try:
            for root, dirs, files in os.walk("../Images/Rename_images/"):
                for filename in files:
                    # print(filename)
                    preImagesName.insert(index, filename)
                    index += 1

                start_number = 1  # number will be changed according to start number
                for x in range(0, len(preImagesName)):
                    print(x)
                    before_name = 'img_'
                    ext = '.jpg'
                    newImagesName.insert(x, before_name + str(start_number) + ext)
                    start_number += 1

                for x in range(0, len(preImagesName)):
                    os.rename(os.path.join(directory, preImagesName[x]), os.path.join(directory, newImagesName[x]))
                    print(newImagesName[x])

            messagebox.showinfo("Success", "Successfully renamed!")
        except:
            messagebox.showerror("Fail", "Error occured!")

    def test(self):
        preImagesName = []
        newImagesName = []
        index = 0
        directory = '../Images/Rotate_image/'


        for root, dirs, files in os.walk("../Images/Rotate_image/"):
            for filename in files:
                # print(filename)
                preImagesName.insert(index, filename)
                img1 = cv2.imread("../Images/Rotate_image/" + preImagesName[index])
                #img1.rotate(90)
                #m = np.arange(8).reshape((2, 2, 2))
                img2 = np.rot90(img1)
                cv2.imwrite(os.path.join(directory, preImagesName[index]), img2)
                print(preImagesName[index])
                index += 1

            start_number = 10  # number will be changed according to start number
            for x in range(0, len(preImagesName)):
                print(x)
                before_name = 'img_'
                ext = '.jpg'
                newImagesName.insert(x, before_name + str(start_number) + ext)
                start_number += 1

            for x in range(0, len(preImagesName)):
                os.rename(os.path.join(directory, preImagesName[x]), os.path.join(directory, newImagesName[x]))
                print(newImagesName[x])

            #messagebox.showinfo("Success", "Successfully renamed!")

            #messagebox.showerror("Fail", "Error occured!")



    # make multidimentional list to store feature values
    def CreateFeaturesMultiDimentionList(self, *arr, folderPath):
        folderPathIndex = folderPath
        csvFilePath = ''
        successMessage = 1
        featureList = []
        lengthOfArray = len(arr[0])
        count = int(lengthOfArray / 257) + 1
        count1 = 0

        indexNo = 0
        # get the index for set of features list
        countArray = []
        for x in range(0,count):
            countArray.insert(x, indexNo)
            indexNo = indexNo + 1
        #print(countArray)

        indexNum = 0
        # give titles to feature vectors
        titleArray = []
        for x in range(0, 257):
            if x == 0:
                titleArray.insert(x, "ImageName")
            else:
                title = 'v_' + str(indexNum)
                titleArray.insert(x, title)
            indexNum = indexNum + 1
        #print(titleArray)

        startIndex = 0
        endIndex = 257
        for i in countArray:
            featureList.append([])
            if i * 257 == startIndex:
                count1 = 0
            #print("startIndex"+str(startIndex))
            for j in range(startIndex, endIndex):
                if i == 0:
                    # insert title to multidimensional list
                    featureList[0].append(titleArray[j])
                else:
                    # add other feature vectors to multidimensional list
                    featureList[i].append(arr[0][j])
                #print("index ="+str(count1)+" "+str(arr[0][j]))
                count1 = count1 + 1
            if i == 0:
                startIndex = 0
                endIndex = 257
            else:
                startIndex = startIndex + 257
                endIndex = endIndex + 257

        #print(featureList)

        # identify the csv file location
        if folderPathIndex == 1:
            csvFilePath = '../Features/Lab_features.csv'
        if folderPathIndex == 2:
            csvFilePath = '../Features/HSV_features.csv'
        if folderPathIndex == 3:
            csvFilePath = '../Features/Gray_features.csv'
        if folderPathIndex == 4:
            csvFilePath = '../Features/Original_images_features.csv'

        # insert feature values to csv file
        try:
            with open(csvFilePath, mode='w', newline='') as feature_file:
                feature_writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                for i in featureList:
                    # print(i)
                    feature_writer.writerow(i+['Label'])
            successMessage = 1
        except:
            successMessage = 0

        return successMessage

    # function for show notification message (Success or Fail)
    def csvFileCreationNotificationMessage(self, successIndex, category):
        categoryName = ''
        if category == 1:
            categoryName = 'L*a*b'
        if category == 2:
            categoryName = 'HSV'
        if category == 3:
            categoryName = 'Gray'
        if category == 4:
            categoryName = 'Original'

        if successIndex == 1:
            messagebox.showinfo("Success", "Successfully created "+ categoryName+ " csv file!")
        if successIndex == 0:
            messagebox.showerror("Fail", "Error occured with "+ categoryName + " file!")



        