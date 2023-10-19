from PIL import Image

class CImage:
    def __init__(self, filename):
        self.fname = filename
        with Image.open(self.fname) as self.img:
            self.img.load()