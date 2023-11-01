# CImage
Python-Class for working with images based in Pillow library

Class **CImge** is designed to work with color and black/white images
## Attributes 
* **fname** - name of the image in the system. For example, *"name-of-image.jpg"*.

* **mode** - the mode in which the image was taken. Can be 'L' - black and white, and 'RGB - color image.

* **width** - width of image in pixels

* **height** - height of image in pixels

## Methods of class

### change_contrast
Method is intended to change contrast or brightness of image

**Input:**

* **contrast** - parameter for changhing contrast
    
* **brightness** - parameter for changhing brightness
    
**Output:** an image to which the method has been applied with changed contrast and brightness


 The ImageProcessor class provides methods for processing and manipulating images.
    Methods:
    
1. invert_image(cls, image_path)
        Inverts the colors of the provided image and displays the result.
        Parameters:
        - cls: The class itself (automatically provided by the @classmethod decorator).
        - image_path (str): The path to the input image file.
2. overlay_with_transparency(cls, base_image_path, overlay_image_path, alpha)
        Overlays two images with a specified alpha (transparency) value and displays the result.

Parameters:
        - cls: The class itself (automatically provided by the @classmethod decorator).
        - base_image_path (str): The path to the base image file.
        - overlay_image_path (str): The path to the overlay image file.
        - alpha (float): The transparency level (0.0 for fully transparent, 1.0 for fully opaque).

Usage:
    1. Invert an image:
       image_path (str): Path to the image you want to invert.
    2. Overlay two images with transparency:
       base_image_path (str): Path to the base image.
       overlay_image_path (str): Path to the overlay image.
       alpha (float): Transparency level for the overlay (0.0 to 1.0).
   
### 
