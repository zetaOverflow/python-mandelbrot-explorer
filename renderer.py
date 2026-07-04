import numpy as np
from PIL import Image

def RenderFractal(res, scale, max_iter, fractalX, fractalY):
    width = res
    height = res
    x_range = 1/scale
    y_range = 1/scale
    img = np.zeros((height, width, 3), dtype=np.uint8)

    def itter(cRealPart, cImaginaryPart, itterations):
        zRealPart = 0
        zImaginaryPart = 0
        for i in range(itterations):
            magnitude = zRealPart**2 + zImaginaryPart**2
            if(magnitude > 4):
                break             
            new_zReal = zRealPart**2 - zImaginaryPart**2 + cRealPart
            new_zImag = 2*zRealPart*zImaginaryPart + cImaginaryPart
            zRealPart = new_zReal
            zImaginaryPart = new_zImag
        return(magnitude, i) 

    for py in range(height):
        y = 2*y_range*((py/height)-0.5) + fractalY
        for px in range(width):
            #Calculation For 1 Pixel
            x = 2*x_range*((px/width)-0.5) + fractalX
            mag, itterations = itter(x, y, max_iter)
            
            #Shading
            if(mag > 4):
                mu = itterations + 1 - np.log2(np.log2(mag))
                t = (mu / 25)
                shade = int(t * 255)
                shade = max(0, min(255, shade))
                img[py, px] = [
                    min(255, int(shade*r)),
                    min(255, int(shade*g)),
                    min(255, int(shade*b))
                ]
            else:
                img[py, px] = [255, 255, 255]
                
    image = Image.fromarray(img)
    return(image)
       
# Creating Image
r, g, b = 1, 0.5, 1
image = RenderFractal(800, 0.5, 100, 0, 0) # Format: RenderFractal(res, scale, max_iter, fractalX, fractalY)
image.save("mandelbrot.png")
image.show()


"""
Cool Places to Zoom into :
  Seahorse Valley:
  fractalX = -0.743643887037151
  fractalY = 0.131825904205330
  scale = 100
  
  Elephant Valley:
  fractalX = 0.282
  fractalY = 0.01
  scale = 30
  
  Mini Mandelbrot:
  fractalX = -1.25066
  fractalY = 0.02012
  scale = 500
"""