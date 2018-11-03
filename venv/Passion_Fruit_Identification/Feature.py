import cv2 as cv2
import numpy as np
import matplotlib as plt
import csv

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

        # with open('../Features/features.csv', 'wb') as csvfile:
        #     filewriter = csv.writer(csvfile, delimiter=',',
        #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     filewriter.writerow(['Name', 'Profession'])
        #     filewriter.writerow(['Derek', 'Software Developer'])
        #     filewriter.writerow(['Steve', 'Software Developer'])
        #     filewriter.writerow(['Paul', 'Manager'])

        image_feature_array = []
        image_feature_array.insert(0,img)
        for i in range(1,257):
            image_feature_array.insert(i,hist_lbp[i-1][0])
        return image_feature_array # image name + 256 textures

        # with open('../Features/features.csv', 'w') as filehandle:
        #     filehandle.write('%s=>' % img)
        #     for x in hist_lbp:
        #         filehandle.write('%s,' % x[0])
        #     filehandle.write('\n')
        #
        # print(img)
        # print(hist_lbp)
        # print("------------------------------------------")

    # get all images features values into one list
    def GetFeatureValues(self, image_name, image_path):
        img_name = image_name
        img_path = image_path
        features_list = []
        startIndex = 0
        endIndex = 0
        arrayLength = 0

        feature_array = Feature.FeatureExtraction(self,img_name,img_path)
        arrayLength = len(feature_array)
        endIndex = endIndex + arrayLength
        for i in range(startIndex, endIndex):
            features_list.insert(i, feature_array[i])
        return features_list

    def test(self):
        person = [['SN', 'Person', 'DOB'],
                  ['1', 'John', '18/1/1997'],
                  ['2', 'Marie', '19/2/1998'],
                  ['3', 'Simon', '20/3/1999'],
                  ['4', 'Erik', '21/4/2000'],
                  ['5', 'Ana', '22/5/2001']]

        csv.register_dialect('myDialect',
                             quoting=csv.QUOTE_ALL,
                             skipinitialspace=True)

        with open('../Features/features.csv', 'w') as f:
            writer = csv.writer(f, dialect='myDialect')
            for row in person:
                writer.writerow(row)

    # make multidimentional list to store feature values
    def CreateFeaturesMultiDimentionList(self, *arr):
        featureList = []
        lengthOfArray = len(arr[0])
        count = int(lengthOfArray / 257)
        count1 = 0

        indexNo = 0
        countArray = []
        for x in range(0,count):
            countArray.insert(x, indexNo)
            indexNo = indexNo + 1
        print(countArray)

        indexNum = 0
        titleArray = []
        for x in range(0, 257):
            if x == 0:
                titleArray.insert(x, "ImageName")
            else:
                title = 'value' + str(indexNum)
                titleArray.insert(x, title)
            indexNum = indexNum + 1
        print(titleArray)

        startIndex = 0
        endIndex = 257
        for i in countArray:
            featureList.append([])
            if i * 257 == startIndex:
                count1 = 0
            print("startIndex"+str(startIndex))
            for j in range(startIndex, endIndex):
                if i == 0:
                    featureList[0].append(titleArray[j])
                else:
                    featureList[i].append(arr[0][j])
                #print("index ="+str(count1)+" "+str(arr[0][j]))
                count1 = count1 + 1
            startIndex = startIndex + 257
            endIndex = endIndex + 257

        print(featureList)

        # for i in range(0,257):
        #     featureList.append([])
        #     featureList.insert(i, arr[0][i])
        #     # for j in range(startIndex, endIndex):
        #     #     featureList[]
        # print(featureList)

        # arr = []
        # arr.append([])
        # arr[0].append('aa1')
        # arr[0].append('aa2')



        