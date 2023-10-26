from PIL import Image
from numpy import sqrt
from numpy import ones
from math import exp

def change_contrast(img_in, contrast, brightness):
        wid, hei = img_in.size
        img_out = Image.new('L', (wid,hei))
        for pixX in range(wid):
            for pixY in range(hei):
                pxl = int(contrast*img_in.getpixel((pixX,pixY))) + brightness
                img_out.putpixel((pixX,pixY), pxl)

        return img_out


def zero_padding(img, size):
    wid, hei = img.size
    img_out = Image.new('L',(wid+2*size,hei+2*size))
    for pixX in range(wid):
        for pixY in range(hei):
            pxl = img.getpixel((pixX,pixY))
            img_out.putpixel((pixX+size,pixY+size), pxl)

    return img_out

def gauss_filter(img, size_kernel = 5):
    wid, hei = img.size
    img_pad = zero_padding(img, size_kernel-1)
    img_out = Image.new('L',(wid,hei))

    for pixX in range(wid):
        for pixY in range(hei):
            pxl_new = gauss_kernel(img_pad, pixX, pixY, size_kernel)
            img_out.putpixel((pixX,pixY), int(pxl_new))

    return img_out

def gauss_kernel(img, x, y, size_kernel):
    kernel = ones([size_kernel,size_kernel])
    sigma = 1
    bound = int((size_kernel - 1) / 2)
    for i in range(-bound,bound+1):
        for j in range(-bound,bound+1):
            kernel[i+bound][j+bound] = exp(- (i*i+j*j) / 2 / sigma / sigma) / 2/3.14/sigma/sigma
    pxl_new = 0
    for i in range(-bound,bound+1):
        for j in range(-bound,bound+1):
            pxl = img.getpixel((x + i, y + j))
            pxl_new = pxl_new + pxl * kernel[i+bound][j+bound]

    return pxl_new

def edge_det(img, xory = 'xy', size_kernel = 3):
    wid, hei = img.size
    img_pad = zero_padding(img, int((size_kernel-1)/2))
    img_out = Image.new('L',(wid,hei))

    for pixX in range(wid):
        for pixY in range(hei):
            if xory == 'xy': 
                pxl_x = edge_kernel(img_pad, pixX, pixY, size_kernel, 'x')
                pxl_y = edge_kernel(img_pad, pixX, pixY, size_kernel, 'y')
                pxl_new = sqrt(pxl_x**2 + pxl_y**2)
            else:
                pxl_new = edge_kernel(img_pad, pixX, pixY, size_kernel, xory)

            img_out.putpixel((pixX,pixY), int(pxl_new))

    return img_out

def edge_kernel(img, x, y, size_kernel, xory):
    if xory == 'x':
        kernel = [[1,2,1], [0,0,0], [-1,-2,-1]]
    else:
        kernel = [[1,0,-1], [2,0,-2], [1,0,-1]]
    
    pxl_new = 0
    for i in range(size_kernel):
        for j in range(size_kernel):
            pxl = img.getpixel((x + i, y + j))
            pxl_new = pxl_new + pxl * kernel[i][j]

    return pxl_new
    

class CImage:
    def __init__(self, filename):
        self.fname = filename
        with Image.open(self.fname) as self.img:
            self.img.load()

        self.mode = self.img.mode
        self.width, self.height = self.img.size

    def show(self):
        self.img.show()

    def change_contrast(self, contrast, brightness):
        if self.mode == 'L':
            self.img = change_contrast(self.img, contrast, brightness)
        else:
            r, g, b = self.img.split()
            r = change_contrast(r, contrast, brightness)
            g = change_contrast(g, contrast, brightness)
            b = change_contrast(b, contrast, brightness)
            self.img = Image.merge('RGB', (r,g,b))

        return self
    
    def gauss_blurring(self):
        if self.mode == 'L':
            self.img = gauss_filter(self.img)
        else:
            r, g, b = self.img.split()
            r = gauss_filter(r)
            g = gauss_filter(g)
            b = gauss_filter(b)
            self.img = Image.merge('RGB', (r,g,b))

        return self
    
    def edge_detection(self):
        img_out = Image.new(self.mode,(self.width,self.height))
        if self.mode == 'L':
            img_out = edge_det(self.img)
        else:
            r, g, b = self.img.split()
            r = edge_det(r)
            g = edge_det(g)
            b = edge_det(b)
            img_out = Image.merge('RGB', (r,g,b))

        return img_out