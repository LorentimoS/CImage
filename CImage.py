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
if __name__ == "__main__":
    image_path = ''
    ImageProcessor.invert_image(image_path)

    base_image_path = ""
    overlay_image_path = ""
    alpha = 0.5
    result_image = ImageProcessor.overlay_with_transparency(base_image_path, overlay_image_path, alpha)
