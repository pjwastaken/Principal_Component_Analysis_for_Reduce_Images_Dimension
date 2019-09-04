import numpy as np
import cv2
import scipy.linalg as a_linalg

class my_algo:
    def __init__(self,image_matrix,image_labels,image_targets,no_of_elments,images_width,images_height,quality_percent)
    self.image_matrix=image_matrix
    self.image_labels=image_labels
    self.image_targets=image_targets
    self.no_of_elments=no_of_elments
    self.images_width=images_width
    self.images_height=images_height
    self.quality_percent=quality_percent

    mean=np.mean(self.image_matrix,1)
    self.mean_face=np.asmatrix(mean).T
    self.image_matrix-=self.mean_face

