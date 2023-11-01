from PIL import Image
from PIL import ImageDraw
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


def frame_by_points(img, x1,y1, x2,y2, color):
    draw = ImageDraw.Draw(img)

    line_color = color
    line_width = 2

    draw.line([x1,y1, x2,y1, x2,y2, x1,y2, x1,y1], 
              fill = line_color, width = line_width)

    return img


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
    
    def draw_frame(self, x1,y1, x2,y2, color):
        if self.mode == 'L':
            self.img = frame_by_points(self.img, x1,y1, x2,y2, color)
        else:
            r, g, b = self.img.split()
            r = frame_by_points(r, x1,y1, x2,y2, color[0])
            g = frame_by_points(g, x1,y1, x2,y2, color[1])
            b = frame_by_points(b, x1,y1, x2,y2, color[2])
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

class ImageProcessor:
    @classmethod
    def invert_image(cls, image_path):
        image = Image.open(image_path)
        image = image.convert('RGBA')
        width, height = image.size
        inverted_image = Image.new('RGBA', (width, height))

        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                inverted_pixel = tuple(255 - value for value in pixel[:3]) + (pixel[3],)
                inverted_image.putpixel((x, y), inverted_pixel)

        inverted_image.show()

    @classmethod
    def overlay_with_transparency(cls, base_image_path, overlay_image_path, alpha):
        base_image = Image.open(base_image_path)
        overlay_image = Image.open(overlay_image_path)
        base_image = base_image.convert('RGBA')  
        overlay_image = overlay_image.convert('RGBA')  
        overlay_image = overlay_image.resize(base_image.size)
        img_out = Image.new(base_image.mode, base_image.size)

        for x in range(base_image.width):
            for y in range(base_image.height):
                base_color = base_image.getpixel((x, y))
                overlay_color = overlay_image.getpixel((x, y))

                final_color = (
                    int((1 - alpha) * base_color[0] + alpha * overlay_color[0]),
                    int((1 - alpha) * base_color[1] + alpha * overlay_color[1]),
                    int((1 - alpha) * base_color[2] + alpha * overlay_color[2]),
                    int((1 - alpha) * base_color[3] + alpha * overlay_color[3])
                )

                img_out.putpixel((x, y), final_color)
        img_out.show()
        return img_out
