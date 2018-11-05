import numpy as np
import cv2 as cv2
import matplotlib.pyplot
import glob
import os

class Image(object):

    # def __init__(self):
    #     kk

    # image preprocessing function
    def ImagePreprocessing(self, img_name):
        # load a colour image
        img = img_name
        print(img)
        img1 = cv2.imread("../Images/Images_Original/"+img)
        height = np.size(img1, 0)
        width = np.size(img1, 1)
        # horizontal images are rotated to vertical
        if height<width:
            img2 = np.rot90(img1)
            # resize the image
            resized_image1 = cv2.resize(img2, (400, 600))
        else:
            # resize the image
            resized_image1 = cv2.resize(img1, (400, 600))
        if height == width:
            # resize the image
            resized_image1 = cv2.resize(img1, (400, 600))

        # remove noise from colour image
        preprocessed_image = cv2.fastNlMeansDenoisingColored(resized_image1, None, 10, 10, 7, 21)
        cv2.imwrite('../images/Images_Preprocessed/' + img, preprocessed_image)

    # image segmentation function
    def ImageSegmentation(self, img_name):
        k_values = [2,4,6,8]
        # colour pattern => 0=original, 1=Lab, 2=HSV, 3=Gray
        color_pattern = [0,1,2,3]
        imgName = img_name
        img_name = imgName[0:5]
        img_ext = imgName[5:9]

        img = cv2.imread("../Images/Images_Preprocessed/" + imgName)
        orginal_image = img
        lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Removing early saved jpg files
        # files = glob.glob('../images/All_Segmented_Images/*.jpg')
        # for f in files:
        #     os.remove(f)

        #k-means clustering called for different k values
        for k in k_values:
            for clrptn in color_pattern:
                if clrptn == 0:
                    Z = orginal_image.reshape((-1, 3))
                    # convert to np.float32
                    Z = np.float32(Z)
                    # define criteria, number of clusters(K) and apply kmeans()
                    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                    # Now convert back into uint8, and make original image
                    center = np.uint8(center)
                    res = center[label.flatten()]
                    res2 = res.reshape((orginal_image.shape))
                    cv2.imwrite('../images/All_Segmented_Images/'+img_name+"_0_"+str(k)+img_ext, res2)
                    cv2.imwrite('../images/Segmented_images/Original/' + img_name + "_0_" + str(k) + img_ext, res2)
                if clrptn == 1:
                    Z = lab_image.reshape((-1, 3))
                    # convert to np.float32
                    Z = np.float32(Z)
                    # define criteria, number of clusters(K) and apply kmeans()
                    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                    # Now convert back into uint8, and make original image
                    center = np.uint8(center)
                    res = center[label.flatten()]
                    res2 = res.reshape((lab_image.shape))
                    cv2.imwrite('../images/All_Segmented_Images/'+img_name+"_1_"+str(k)+img_ext, res2)
                    cv2.imwrite('../images/Segmented_images/Lab/' + img_name + "_1_" + str(k) + img_ext, res2)
                if clrptn == 2:
                    Z = hsv_image.reshape((-1, 3))
                    # convert to np.float32
                    Z = np.float32(Z)
                    # define criteria, number of clusters(K) and apply kmeans()
                    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                    # Now convert back into uint8, and make original image
                    center = np.uint8(center)
                    res = center[label.flatten()]
                    res2 = res.reshape((hsv_image.shape))
                    cv2.imwrite('../images/All_Segmented_Images/'+img_name+"_2_"+str(k)+img_ext, res2)
                    cv2.imwrite('../images/Segmented_images/HSV/' + img_name + "_2_" + str(k) + img_ext, res2)
                if clrptn == 3:
                    Z = gray_image.reshape((-1, 3))
                    # convert to np.float32
                    Z = np.float32(Z)
                    # define criteria, number of clusters(K) and apply kmeans()
                    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
                    # Now convert back into uint8, and make original image
                    center = np.uint8(center)
                    res = center[label.flatten()]
                    res2 = res.reshape((gray_image.shape))
                    cv2.imwrite('../images/All_Segmented_Images/'+img_name+"_3_"+str(k)+img_ext, res2)
                    cv2.imwrite('../images/Segmented_images/Gray/' + img_name + "_3_" + str(k) + img_ext, res2)
        print(img_name + "'s segmentation was done")


