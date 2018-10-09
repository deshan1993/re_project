import numpy as np
import cv2 as cv2
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from Image import Image
from Feature import Feature

class Main:

    def main():

        image = Image()
        feature = Feature()

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

        def featureExtract():

            foldersPath = ["../Images/Segmented_Images/Original/",
                          "../Images/Segmented_Images/Lab/",
                          "../Images/Segmented_Images/HSV/",
                          "../Images/Segmented_Images/Gray/"]

            for folderPath in foldersPath:
                imagesName = gettingImages(folderPath)
                for imageName in imagesName:
                    #print("path = " + folderPath + "   " + imageName)
                    feature.FeatureExtraction(img_name=imageName, img_path=folderPath)
                    #messagebox.showinfo("Success", "Successfully features were extracted")


        preprocess_btn = Button(text="Preprocessing", command = preprocess)
        preprocess_btn.place(x=10,y=10)

        segment_btn = Button(text="Segmentation", command = segment)
        segment_btn.place(x=10, y=50)

        segment_btn = Button(text="Feature Extraction", command=featureExtract)
        segment_btn.place(x=10, y=90)
        root.mainloop()



    if __name__ == '__main__':
        main()


