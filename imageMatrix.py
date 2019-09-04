import cv2
import numpy as np

class imageToMatrixClass:

    def __init__(self,images_path,images_width,images_height):
        self.images_path=images_path
        self.images_width=images_width
        self.images_height=images_height
        self.images_size=images_width*images_height

    def get_matrix(self):
        
        col=len(self.images_path)
        img_mat=np.zeros((self.images_size,col))

        i=0
        for path in self.images_path:
            gray=cv2.imread(path,0)
            gray_resized=cv2.resize(gray,(self.images_width,self.images_height))
            mat_gray=np.asmatrix(gray_resized)
            vec=mat_gray.ravel()

            img_mat[:,i]=vec
            i+=1
        return img_mat