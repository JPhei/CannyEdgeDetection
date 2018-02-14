'''
  File name: findDerivatives.py
  Author: Hantian Liu
  Date created: 09/2017
'''

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''
import numpy as np
import math
import scipy.signal
import utils

def findDerivatives(I_gray):
  # TODO: your code here
  
  # Gaussian filter
  #G = np.array([[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]])
  #G = np.matrix('2,4,5,4,2; 4,9,12,9,4; 5,12,15,12,5; 4,9,12,9,4; 2,4,5,4,2') #sigma=1.4
  #G = G/159;
  #Ga = np.squeeze(np.asarray(G))
  
  #less sigma, more blurred edge 
  mu=0
  sigma=0.4 #0.4
  Ga = utils.GaussianPDF_2D(mu, sigma, 5, 5)
  
  # Filter 
  dx = np.array([[1, 0, -1]]) # Horizontal
  dy = np.array([[1], [0], [-1]]) # Vertical
  #dx = np.array([[1, -1]]) # Horizontal
  #dy = np.array([[1],[-1]]) # Vertical
  
  # Convolution of image
  #Gx = np.convolve(G, dx, 'same')
  #Gy = np.convolve(G, dy, 'same')
  #lx = np.convolve(I_gray, Gx, 'same')
  #ly = np.convolve(I_gray, Gy, 'same')
  
  Gx = scipy.signal.convolve2d(Ga, dx, boundary='fill', mode='same')
  Gy = scipy.signal.convolve2d(Ga, dy, boundary='fill', mode='same')
  lx = scipy.signal.convolve2d(I_gray, Gx, boundary='fill', mode='same')
  ly = scipy.signal.convolve2d(I_gray, Gy, boundary='fill', mode='same')
  
  # Magnitude
  Mag = np.sqrt(lx*lx+ly*ly)
  
  # Angle
  angle = np.arctan(ly/lx)
  angle[angle<0] = math.pi + angle[angle<0]
  angle[angle>7*math.pi/8] = math.pi - angle[angle>7*math.pi/8]
  '''
  # Edge angle discretization into 0, pi/4, pi/2, 3*pi/4
  angle[angle>=0 and angle<math.pi/8] = 0
  angle[angle>=math.pi/8 and angle<3*math.pi/8] = math.pi/4
  angle[angle>=3*math.pi/8 and angle<5*math.pi/8] = math.pi/2
  angle[angle>=5*math.pi/8 and angle<=7*math.pi/8] = 3*math.pi/4
  '''
  
  return (Mag, lx, ly, angle) 
