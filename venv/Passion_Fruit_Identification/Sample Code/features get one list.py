def featureExtract():
    features_list = []
    startIndex = 0
    endIndex = 0
    arrayLength = 0
    count = 0

    foldersPath = ["../Images/Segmented_Images/Original/",
                   "../Images/Segmented_Images/Lab/",
                   "../Images/Segmented_Images/HSV/",
                   "../Images/Segmented_Images/Gray/"]

    for folderPath in foldersPath:
        imagesName = gettingImages(folderPath)
        for imageName in imagesName:
            count = count + 1
            count1 = 0
            # feature.GetFeatureValues(image_name=imageName, image_path=folderPath)
            # print("path = " + folderPath + "   " + imageName)
            feature_array = feature.FeatureExtraction(img_name=imageName, img_path=folderPath)
            arrayLength = len(feature_array) * count
            endIndex = arrayLength - 1
            startIndex = endIndex - 256
            print("startIndex = " + str(startIndex) + ", endIndex = " + str(endIndex) + ", arrayLength = " + str(
                arrayLength))
            # j = (endIndex - (257*count)) + 1
            for i in range(startIndex, endIndex + 1):
                if count1 == 257 * count:
                    count1 = 0
                # print(str(i)+" = "+str(feature_array[count1]))
                features_list.insert(i, feature_array[count1])
                count1 = count1 + 1
                # print(str(i)+" = "+str(feature_array[((endIndex - (257*count)) + 1 +i)]))
                # features_list.insert(i, feature_array[((endIndex - (257*count)) + 1 +i)])
            # return features_list
            # messagebox.showinfo("Success", "Successfully features were extracted")

    csv.register_dialect('myDialect',
                         quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)

    with open('../Features/features.csv', 'wb') as f:
        writer = csv.writer(f, dialect='myDialect')
        for row in features_list:
            writer.writerow(row)
    # print(features_list)