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


### gauss_blurring
The method is intended to blur an image using a Gaussian kernel

**Input:**

* **self** - the image to which the method is applied
    
**Output:** an oject of class with image to which the method of blurring has been applied. Also change original image of class!


### edge_detection
The method is intended to find the boundaries of depicted objects

**Input:**

* **self** - the image to which the method is applied
    
**Output:** an image to which the method has been applied. This is black image with white edges of objects.
