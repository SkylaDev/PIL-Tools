from . import core
from PIL import Image, ImageDraw, ImageOps


class ImageTools:
    def __init__(self, image: Image.Image):
        """
        Create a drawing instance.

        :param image: The image to draw in.
        """

        image.load()
        if image.readonly:
            image.copy()

        self.image = image

        # Any aliases for functions
        self.greyscale = self.grayscale

    def black_and_white(self, threshold: int=150):
        """
        Converts replaces the colour in the image with just black and white without changing the base image mode.

        :param threshold: int (The threshold for the selection between black and white, the higher the threshold the more black the image will be. (default 150))
        """

        self.image.paste(self.image.convert("L").point(lambda x: 255 if x > threshold else 0, mode='1'))

    def grayscale(self):
        """
        Converts replaces the colour in the image with shades of gray without changing the base image mode.
        """

        self.image.paste(self.image.convert("L"))

    def invert(self):
        """
        Inverts the colours on the base image (supports transparency).
        """

        if self.image.mode == "RGBA":
            r, g, b, a = self.image.split()
            rgb = Image.merge("RGB", (r, g, b))

            inv = ImageOps.invert(rgb)
            r2, g2, b2 = inv.split()

            image = Image.merge("RGBA", (r2, g2, b2, a))
        else:
            image = ImageOps.invert(self.image)

        self.image.paste(image, (0, 0))

    def rounded_edges(self, radius: int, fill: tuple=None, inverted: bool=False, tl: bool=True, tr: bool=True, bl: bool=True, br: bool=True):
        """
        Adds a rounded edge effect to the image.

        :param radius: int (Radius of the edges in pixels.)
        :param fill: (Colour to fill corners with, makes transparent if None (black if image not in transparent friendly mode like RGBA.))
        :param inverted: bool (Determines if the mask covers the inside or outside of box.)
        :param tl: bool (Determines whether the top left corner is rounded.)
        :param tr: bool (Determines whether the top right corner is rounded.)
        :param bl: bool (Determines whether the bottom left corner is rounded.)
        :param br: bool (Determines whether the bottom right corner is rounded.)
        """

        self.image.paste(Image.new(self.image.mode, self.image.size, fill if fill else 0), (0, 0), core.rounded_edge_mask(self.image.size, radius, inverted, tl, tr, bl, br))

