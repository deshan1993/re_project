import numpy as np
import cv2 as cv2
import os
import tkinter
import csv

class Label(object):

    def getImagesNames(self):
        imagesName = []
        folderPath = "../Images/Images_Original/"
        for root, dirs, files in os.walk(folderPath):
            # make array using img names ex: img_1, img_2
            for filename in files:
                imagesName.append(filename.split('.',1)[0])
        #print(imagesName)
        return imagesName


    def allocateLabel(self):
        # csvFilePath = '../Label/Label_file.csv'
        # imagesName = Label.getImagesNames(self)
        # with open(csvFilePath, mode='w', newline='') as label_file:
        #     label_writer = csv.writer(label_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #     label_writer.writerow(['Name','Label'])
        #     for i in imagesName:
        #         # print(i)
        #         label_writer.writerow(i.split())
        # print(imagesName)

        with open("../Features/Lab_features.csv") as feature:
            featureList = csv.reader(feature)
            for featureRow in featureList:
                imgName = '_'.join(featureRow[0].split('_',2)[:2])

                with open("../Label/Label_file.csv") as label:
                    labelList = csv.reader(label)
                    for labelRow in labelList:
                        if labelRow[0] == imgName:
                            featureRow[257] = labelRow[1]
                            writer = csv.writer(open('../Features/Lab_features.csv', 'w'))
                            #writer.writerows(featureRow) #error
                            print("success")

        # with open('../Label/Label_file.csv') as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     line_count = 0
        #
        #     for row in csv_reader:
        #         if line_count == 0:
        #             print(row[0])
        #             line_count = line_count + 2