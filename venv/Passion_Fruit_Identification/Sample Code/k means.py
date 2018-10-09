import numpy as np
import cv2
import matplotlib.pyplot
import numpy as np

img = cv2.imread("../../Images/Images_Original/img_5.jpg")
resized_image = cv2.resize(img, (400, 600))
#lab_image1 = cv2.cvtColor(resized_image, cv2.COLOR_HSV2BGR)
lab_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)
Z = lab_image.reshape((-1, 3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((lab_image.shape))
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()