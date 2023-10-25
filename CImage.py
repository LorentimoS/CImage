from PIL import Image

def change_contrast(img_in, contrast, brightness):
        wid, hei = img_in.size
        img_out = Image.new('L', (wid,hei))
        for pixX in range(wid):
            for pixY in range(hei):
                pxl = int(contrast*img_in.getpixel((pixX,pixY))) + brightness
                img_out.putpixel((pixX,pixY), pxl)

        return img_out
    

class CImage:
    def __init__(self, filename):
        self.fname = filename
        with Image.open(self.fname) as self.img:
            self.img.load()

        self.mode = self.img.mode
        self.width, self.height = self.img.size

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

def invert_image(base_image_path):
    image = Image.open(base_image_path)
    width, height = image.size
    inverted_image = Image.new('RGB', (width, height))
        
    for pixY in range(height):
        for pixX in range(width):
            pixel = image.getpixel((pixX, pixY))
            inverted_pixel = tuple(255 - value for value in pixel)
            inverted_image.putpixel((pixX, pixY), inverted_pixel)
    inverted_image.show()
result_image = ' '
invert_image(base_image_path)


def overlay_with_transparency(base_image_path, overlay_image_path, alpha):
  
    base_image = Image.open(base_image_path)
    overlay_image = Image.open(overlay_image_path)
    overlay_image = overlay_image.resize(base_image.size)
    img_out = Image.new(base_image.mode, base_image.size)

    for pixX in range(base_image.width):
        for y in range(base_image.height):
            base_color = base_image.getpixel((pixX, pixY))
            overlay_color = overlay_image.getpixel((pixX, pixY))
            final_color = (
                int((1 - alpha) * base_color[0] + alpha * overlay_color[0]),
                int((1 - alpha) * base_color[1] + alpha * overlay_color[1]),
                int((1 - alpha) * base_color[2] + alpha * overlay_color[2])
            )

            img_out.putpixel((pixX, pixY), final_color)
    img_out.show()
    return img_out
        
result_image = overlay_with_transparency(base_image_path, overlay_image_path, alpha)
alpha = 0.5
base_image_path = " "
overlay_image_path = " "
result_image.save(" ")
