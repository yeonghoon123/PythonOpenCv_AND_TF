import cv2

image = cv2.imread("/home/kyh/Downloads/cat.jpg",cv2.IMREAD_ANYCOLOR)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height,width,channel = image.shape
image90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
image180 = cv2.rotate(image, cv2.ROTATE_180)
image270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# martix_1 = cv2.getRotationMatrix2D((width/2,height/2),90,1)
# martix_2 = cv2.getRotationMatrix2D((width/2,height/2),180,1)
# martix_3 = cv2.getRotationMatrix2D((width/2,height/2),270,1)

# dst1 = cv2.warpAffine(image, martix_1, (width,height))
# dst2 = cv2.warpAffine(image, martix_2,(width,height))
# dst3 = cv2.warpAffine(image, martix_3,(width,height))
cv2.imshow("cat", image)
cv2.imshow("dst1", image90)
cv2.imshow("dst2", image180)
cv2.imshow("dst3", image270)
cv2.waitKey()
cv2.destroyAllWindows()
print(rgb)

