# CImage
Python-Class for working with images based in Pillow library

Class **CImge** is designed to work with color and black/white images
## Attributes 
* **fname** - name of the image in the system. For example, *"name-of-image.jpg"*.

* **mode** - the mode in which the image was taken. Can be 'L' - black and white, and 'RGB - color image.

* **width** - width of image in pixels

* **height** - height of image in pixels

## Methods of class

### show
The method is intended to display the image using a computer application

**Input:**

* **self** - the image to which the method is applied


### change_contrast
The method is intended to change contrast and / or brightness of image

**Input:**

* **self** - the image to which the method is applied

* **contrast** - parameter for changhing contrast
    
* **brightness** - parameter for changhing brightness
    
**Output:** an object of class with image to which the method has been applied with changed contrast and brightness. Also change original image of class!


### draw_frame
The method is intended to draw the frame of some color by two points

**Input:**

* **self** - the image to which the method is applied

* **x1** - the X-coordinate of the first points of frame, top left corner

* **y1** - the Y-coordinate of the first points of frame, top left corner

* **x2** - the X-coordinate of the second points of frame, lower right corner

* **y2** - the Y-coordinate of the second points of frame, lower right corner

* **color** - the color of frame, must be int for black and white images or tuple for color images
    
**Output:** an oject of class with image with drawn frame of given color. Also change original image of class!


### gauss_blurring
The method is intended to blur an image using a Gaussian kernel

**Input:**

* **self** - the image to which the method is applied
    
**Output:** an oject of class with image to which the method of blurring has been applied. Also change original image of class!

### average_blurring
The method is intended to blur an image using a Average kernel

**Input:**

* **self** - the image to which the method is applied
    
**Output:** an oject of class with image to which the method of blurring has been applied. Also change original image of class!

### edge_detection
The method is intended to find edges

**Input:**

* **self** - the image to which the method is applied
    
**Output:** an oject of class with image to which the method has been applied. Also change original image of class!

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

   
### 
