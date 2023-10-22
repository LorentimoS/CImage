# CImage
Python-Class for working with images based in Pillow library

Class **CImge** is designed to work with color and black/white images
## Attributes 
**fname** - name of the image in the system. For example, *"name-of-image.jpg"*.
**mode** - the mode in which the image was taken. Can be 'L' - black and white, and 'RGB - color image.
**width** - width of image in pixels
**height** - height of image in pixels

## Methods of class

### change_contrast
Method is intended to change contrast or brightness of image
**Input parameters:**
    **contrast** - parameter for changhing contrast
    **brightness** - parameter for changhing brightness
**Output** - an image to which the method has been applied with changed contrast and brightness

### 