from mtcnn.mtcnn import MTCNN
# import face_preprocess
import numpy as np
import cv2
import os
from datetime import datetime

detector = MTCNN()
max_faces = 5
max_bbox = np.zeros(4)
print(max_bbox)