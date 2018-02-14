'''
  File name: edgeLink.py
  Author: Hantian Liu
  Date created: 09/2017
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W binary////logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map
'''
import numpy as np
import math

def edgeLink(M, Mag, Ori):
  # TODO: your code here
  M=np.squeeze(np.asarray(M))
  Mag=np.squeeze(np.asarray(Mag))
  Muse=M*Mag
  
  # Hysteresis thresholding
  # for weak edge
  threshold_low = 0.015 #TODO
  threshold_low = threshold_low * Muse.max()
  # for strong edge
  threshold_high = 0.115 #TODO
  threshold_high = threshold_high * Muse.max()
  
  #print(np.sum(Muse))
  #print(np.sum(threshold_low))
  #print(np.sum(threshold_high))
  
  if np.sum(Muse)<50000:
      threshold_low=0.01;
      threshold_high=0.02;
      threshold_low = threshold_low * Muse.max()
      threshold_high = threshold_high * Muse.max()
  elif np.sum(Muse)<250000 and np.sum(threshold_low)>2:
      threshold_low=0.02;
      threshold_high=0.04;
      threshold_low = threshold_low * Muse.max()
      threshold_high = threshold_high * Muse.max()
  elif np.sum(Muse)<550000 and np.sum(threshold_low)>2:
      threshold_low=0.015;
      threshold_high=0.06;
      threshold_low = threshold_low * Muse.max()
      threshold_high = threshold_high * Muse.max()
  
  '''
  (M1,M2,M3,M4,M5,M6)=np.split(Muse, [64,128,192,246,321])
  (M11,M12,M13,M14,M15,M16)=np.split(M1,[96,192,288,384,481],axis=1)
  (M21,M22,M23,M24,M25,M26)=np.split(M2,[96,192,288,384,481],axis=1)
  (M31,M32,M33,M34,M35,M36)=np.split(M3,[96,192,288,384,481],axis=1)
  (M41,M42,M43,M44,M45,M46)=np.split(M4,[96,192,288,384,481],axis=1)
  (M51,M52,M53,M54,M55,M56)=np.split(M5,[96,192,288,384,481],axis=1)
  M11=threshold*M11,max()
  M21=
  '''
  
  
  size = np.shape(Mag)
  E = np.zeros(size)
  #linked_edge = hysteresis_thresholding(threshold_low, threshold_high, linked_edge, ed
  #E= M
  is_weak = Muse>threshold_low
  is_strong = Muse>threshold_high 
  
  for i in range(1, size[0]-1):
      for j in range(1, size[1]-1):
          if E[i,j]==0:
              if is_strong[i,j]:
                  E[i,j]=1
                  if Ori[i,j]==0:
                      if (is_weak[i+1,j]):
                          E[i+1,j]=1 
                      if (is_weak[i-1,j]):
                          E[i-1,j]=1
                  elif Ori[i,j]>0 and Ori[i,j]<math.pi/4:
                      if (is_weak[i+1,j]):
                          E[i+1,j]=1 
                      if (is_weak[i-1,j]):
                          E[i-1,j]=1
                      if (is_weak[i+1,j-1]):
                          E[i+1,j-1]=1
                      if  (is_weak[i-1,j+1]):
                          E[i-1,j+1]=1
                  elif Ori[i,j]==math.pi/4:
                      if (is_weak[i+1,j-1]):
                          E[i+1,j-1]=1
                      if  (is_weak[i-1,j+1]):
                          E[i-1,j+1]=1
                  elif Ori[i,j]>math.pi/4 and Ori[i,j]<math.pi/2:
                      if (is_weak[i+1,j-1]):
                          E[i+1,j-1]=1
                      if  (is_weak[i-1,j+1]):
                          E[i-1,j+1]=1
                      if  (is_weak[i,j+1]):
                          E[i,j+1]==1
                      if (is_weak[i,j-1]):
                          E[i,j-1]==1
                  elif Ori[i,j]==math.pi/2:
                      if  (is_weak[i,j+1]):
                          E[i,j+1]==1
                      if (is_weak[i,j-1]):
                          E[i,j-1]==1
                  elif Ori[i,j]>math.pi/2 and Ori[i,j]<math.pi*3/4:
                      if  (is_weak[i,j+1]):
                          E[i,j+1]==1
                      if (is_weak[i,j-1]):
                          E[i,j-1]==1
                      if (is_weak[i+1,j+1]):
                          E[i+1,j+1]=1
                      if (is_weak[i-1,j-1]):
                          E[i-1,j-1]=1
                  elif Ori[i,j]==math.pi*3/4:
                      if (is_weak[i+1,j+1]):
                          E[i+1,j+1]=1
                      if (is_weak[i-1,j-1]):
                          E[i-1,j-1]=1
                  elif Ori[i,j]>math.pi*3/4:
                      if (is_weak[i+1,j+1]):
                          E[i+1,j+1]=1
                      if (is_weak[i-1,j-1]):
                          E[i-1,j-1]=1
                      if (is_weak[i+1,j]):
                          E[i+1,j]=1 
                      if (is_weak[i-1,j]):
                          E[i-1,j]=1
                                         
  return E
