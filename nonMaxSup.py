'''
  File name: nonMaxSup.py
  Author: Hantian Liu
  Date created: 09/2017
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''
import numpy as np
import math
from scipy import interpolate
from interp import interp2

def nonMaxSup(Mag, Ori):
  # TODO: your code here
  # suppress all the gradient values to 0 except the local maximal
  size = np.shape(Mag)
  Edge = np.zeros(size)
  Edge = np.matrix(Edge)
  threshold = 0
  
  #'''
  #for element in Mag.flat
  #interpolation
  x = np.arange(1, size[0]+1,1)
  y = np.arange(1, size[1]+1,1)
  xx, yy = np.meshgrid(y, x)
  #f = interpolate.interp2d(xx, yy, Mag)

  xnew1 = xx + np.cos(Ori)
  ynew1 = yy + np.sin(Ori)
  xnew2 = xx - np.cos(Ori)
  ynew2 = yy - np.sin(Ori)
  #znew1 = f(xnew1, ynew1)
  znew1=interp2(xx,yy,Mag,xnew1,ynew1)
  #znew2 = f(xnew2, ynew2)
  znew2=interp2(xx,yy,Mag,xnew2,ynew2)
  
  Edge = np.zeros(size)
  Edge1 = np.zeros(size)
  Edge2 = np.zeros(size)
  Edge1[Mag >= znew1+threshold]=1
  Edge2[Mag >= znew2+threshold]=1
  Edge=Edge1*Edge2
  Edge = np.matrix(Edge)
  
  '''
  for x in range(1, size[0]-1):
      for y in range(1, size[1]-1):
          if Ori[x,y]==0:
              if (Mag[x-1, y]+threshold<Mag[x,y] and Mag[x+1, y]+threshold<Mag[x,y]):
                  Edge[x,y]=1
          elif Ori[x,y]==math.pi/4:
              if (Mag[x+1, y+1]+threshold<Mag[x,y] and Mag[x-1, y-1]+threshold<Mag[x,y]):
                  Edge[x,y]=1
          elif Ori[x,y]==math.pi/2:
              if (Mag[x, y+1]+threshold<Mag[x,y] and Mag[x, y-1]+threshold<Mag[x,y]):
                  Edge[x,y]=1
          elif Ori[x,y]==math.pi*3/4:
              if (Mag[x-1, y+1]+threshold<Mag[x,y] and Mag[x+1, y-1]+threshold<Mag[x,y]):
                  Edge[x,y]=1
         # interpolation
          elif Ori[x,y]>0 and Ori[x,y]<math.pi/4:
              r=np.interp(y+math.tan(Ori[x,y]), [y, y+1], [Mag[x+1,y],Mag[x+1,y+1]])
              l=np.interp(y-math.tan(Ori[x,y]), [y-1, y], [Mag[x-1,y-1],Mag[x-1,y]])
              if (Mag[x,y]>r+threshold and Mag[x,y]>l+threshold):
                  Edge[x,y]=1
          elif Ori[x,y]>math.pi/4 and Ori[x,y]<math.pi/2:
              r=np.interp(x+1/math.tan(Ori[x,y]), [x, x+1], [Mag[x,y+1],Mag[x+1,y+1]])
              l=np.interp(x-1/math.tan(Ori[x,y]), [x, x-1], [Mag[x,y-1],Mag[x-1,y-1]])
              if (Mag[x,y]>r+threshold and Mag[x,y]>l+threshold):
                  Edge[x,y]=1
          elif Ori[x,y]>math.pi/2 and Ori[x,y]<math.pi/4*3:
              r=np.interp(x-1/math.tan(math.pi-Ori[x,y]), [x-1, x], [Mag[x-1,y+1],Mag[x,y+1]])
              l=np.interp(x+1/math.tan(math.pi-Ori[x,y]), [x, x+1], [Mag[x,y-1],Mag[x+1,y-1]])
              if (Mag[x,y]>r+threshold and Mag[x,y]>l+threshold):
                  Edge[x,y]=1
          elif Ori[x,y]>math.pi*3/4 and Ori[x,y]<math.pi:
              r=np.interp(y+math.tan(Ori[x,y]), [y, y+1], [Mag[x-1,y],Mag[x-1,y+1]])
              l=np.interp(y-math.tan(Ori[x,y]), [y-1, y], [Mag[x+1,y-1],Mag[x+1,y]])
              if (Mag[x,y]>r+threshold and Mag[x,y]>l+threshold):
                  Edge[x,y]=1
  '''
  return Edge
