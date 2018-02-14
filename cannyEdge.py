'''
  File name: cannyEdge.py
  Author: Haoyuan(Steve) Zhang
  Date created: 9/10/2017
'''

'''
  File clarification:
    Canny edge detector 
    - Input: A color image I = uint8(H, W, 3), where H, W are two dimensions of the image
    - Output: An edge map E = logical(H, W)

    - TO DO: Complete three main functions findDerivatives, nonMaxSup and edgeLink 
             to make your own canny edge detector work
'''

import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import signal
from PIL import Image

# import functions
from findDerivatives import findDerivatives
from nonMaxSup import nonMaxSup
from edgeLink import edgeLink
from Test_script import Test_script
import utils, helpers

import scipy.io as sio #delete

# cannyEdge detector
def cannyEdge(I):
  # convert RGB image to gray color space
  im_gray = utils.rgb2gray(I)

  Mag, Magx, Magy, Ori = findDerivatives(im_gray)
  M = nonMaxSup(Mag, Ori)
  E = edgeLink(M, Mag, Ori)

  # only when test passed that can show all results
  if Test_script(im_gray, E):
    # visualization results
    utils.visDerivatives(im_gray, Mag, Magx, Magy)
    utils.visCannyEdge(I, M, E)

    plt.show()
  #sio.savemat('E3096.mat', {'E':E}) #delete
  return E


if __name__ == "__main__":
  # the folder name that stores all images
  # please make sure that this file has the same directory as image folder
  #folder = 'folder_name'
  folder = 'pic'

  # read images one by one
  for filename in os.listdir(folder):
    # read in image and convert color space for better visualization
    im_path = os.path.join(folder, filename)
    I = np.array(Image.open(im_path).convert('RGB'))
    
    ## TO DO: Complete 'cannyEdge' function
    E = cannyEdge(I)



