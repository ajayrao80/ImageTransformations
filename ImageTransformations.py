import cv2
import math


# Logarithmic Transformations
def log_transform(col, max_pixel_value):
    c = 255/(math.log(1+max_pixel_value))
    new_col = c * math.log(1+col)
    return new_col

def max_pixel(img):
    max_pixel = 0
    height, width, channels = img.shape
    
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if(max_pixel < img[i][j][k]):
                    max_pixel = img[i][j][k]
    
    return max_pixel


# Power law transformation

def powertrans(c, gamma, r):
    #  = C*r^gamma
    new_col = c*((r/c)**gamma)
    return new_col



# Driver code
img = cv2.imread("sample.jpg")

height, width, channels = img.shape
max_pixel_value = max_pixel(img)

for i in range(height):
    for j in range(width):
        for k in range(channels):
            #new_col = 255 - img[i][j][k]
            #new_col = log_transform(img[i][j][k], max_pixel_value)
            new_col = powertrans(255, 0.4, img[i][j][k])
            img[i][j][k] = new_col

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()    




