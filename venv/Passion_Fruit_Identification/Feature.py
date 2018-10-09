import cv2 as cv2
import numpy as np
import matplotlib as plt

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

        with open('../Features/feature_file.txt', 'w') as filehandle:
            filehandle.write('%s=>' % img)
            for x in hist_lbp:
                filehandle.write('%s,' % x[0])
            filehandle.write('\n')

        print(img)
        print(hist_lbp)
        print("------------------------------------------")
        