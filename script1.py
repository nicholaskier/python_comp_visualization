import cv2

img=cv2.imread("galaxy.jpg",0)
# file name, 1 for color or 0 for grayscale or -1 for transparency

print(type(img))
# 2-d array if grayscale, 3-d array for color
print(img.shape)
# px x px

resize_image=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resize_image)
cv2.imwrite("Galaxy_resized.jpg", resize_image)
cv2.waitKey(2000)
# closes window after 2 seconds