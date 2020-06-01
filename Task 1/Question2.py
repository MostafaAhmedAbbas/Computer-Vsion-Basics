#!/usr/bin/env python
# coding: utf-8

# In[123]:


from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import sys

def generateIntegralImage(fileName):
    image = Image.open(fileName)
    gray = image.convert('L')
    img = np.array(gray)
    img2 = np.zeros(img.shape)
    img3 = img.copy()
    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            if(i == 0 and j == 0):
                img2[i][j] = (img[i][j])
            elif(i == 0 and j != 0):
                img2[i][j] = (img2[i][j-1] + img[i][j])
            elif(j == 0 and i != 0):
                img2[i][j] = (img2[i-1][j] + img[i][j])
            else:
                img2[i][j] = (img2[i][j-1] + img2[i-1][j] + img[i][j] - img2[i-1][j-1])
    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            img3[i][j] = (img2[i][j] * 255) / img2[img.shape[0] - 1][img.shape[1] - 1]
#     plt.imshow(img2,cmap="gray")
    savedImage = Image.fromarray(img3,'L')
    savedImage = savedImage.convert('RGB')
    savedImage.save('Camera_Integ.jpg')
    return img2


# In[129]:


from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import sys
# filter
def filter(fileName, size):
    image = Image.open(fileName)
    img3 = image.convert('L')
    img3 = np.array(img3)
    img = generateIntegralImage(fileName)
    img2 = np.zeros(img.shape)
    for i in range ((size//2) + 1,img.shape[0] - (size//2) - 1):
        for j in range (size//2 + 1,img.shape[1] - size//2 - 1):
            img2[i][j] = (img[i+(size//2)][j+(size//2)] + img[i-(size//2) - 1][j-(size//2) - 1] - img[i+(size//2)][j-(size//2)-1] - img[i-(size//2)-1][j+(size//2)]) / (size * size)
    for i in range (0,img.shape[0]):
        for j in range (0,img.shape[1]):
            img3[i][j] = img2[i][j]
    plt.imshow(img3,cmap="gray")
    savedImage = Image.fromarray(img3,'L')
    savedImage = savedImage.convert('RGB')
    savedImage.save("Camera_Filt_" + str(size) + ".jpg")
filter("Cameraman_noise.bmp",3)


# In[ ]:




