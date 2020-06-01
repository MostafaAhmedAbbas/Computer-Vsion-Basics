#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np


# In[5]:


def QuestionOne(a,b,c,d):
    myImage = Image.open("Ocean.BMP")
    # myImage.show()
    newImage = myImage.copy()
    pix = newImage.load()
    size = newImage.size
    x=size[0]
    y=size[1]
    m1 =(b-0)/(a-0)
    m2 =(d-b)/(c-a)
    m3 =(255-d)/(255-c)
    c1=b-(m1*a)
    c2=d-(m2*c)
    c3=255-(m3*255)
    i=0
    while i < x:
        
        z=0
        while z < y:
            
            if  pix[i,z] < a :
                pix[i,z] = int((m1* pix[i,z]) + c1)
            elif pix[i,z] < c :
                 pix[i,z] = int((m2* pix[i,z]) + c2)
            else:
                pix[i,z] = int((m3* pix[i,z]) + c3)

            z += 1
        i += 1
    
    
    return newImage


# In[6]:


newImage = QuestionOne(70,20,140,240)
newImage.save("Ocean_b.bmp")
newImage = QuestionOne(30,20,180,230)
newImage.save("Ocean_a.bmp")


# In[ ]:





# In[11]:


def coOcc():
    
    myImage = Image.open("Ocean.BMP")
    # myImage.show()
    newImage = myImage.copy()
    pix = newImage.load()
    matrix=[[0]*255]*255
    size = newImage.size
    x=size[0] #width
    y=size[1] #height


    # i=0
    # while i< x:
    #     z=0
    #     while z<y-1:
    # #         if(z<y-1):
    #         north = pix[i,z]
    #         south = pix[i,z+1]
    #         print(matrix[north][south])
    #         matrix[north][south] +=1
    #         print(matrix[north][south])

    #         z+=1
    #     i+=1

    for i in range (0,myImage.size[0]):
        for z in range (0,myImage.size[1]-1):
            north = newImage.getpixel((i,z))
            south = newImage.getpixel((i,z+1))
            matrix[north][south] = matrix[north][south] +1



    i=0
    contrast=0
    while i<255:
        z=0
        while z< 255:
            contrast+= matrix[i][z] * ((i-z)**2)
            z+=1
        i+=1
    return(contrast) 


#print('\n'.join([''.join(['{:5}'.format(item) for item in row]) 
 #     for row in matrix]))
        


# In[12]:


coOcc()


# In[ ]:




