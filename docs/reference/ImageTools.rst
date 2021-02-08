The ImageTools module
=====================

The ImageDraw module provides simple 2D effects for
`Image <https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image>`_
objects, this includes some image filters, custom cropping/filling and more.

As well as this this module includes a few utility functions that can help with opening
and handling images from PIL.


Example: Round off corners of an image
--------------------------------------

.. code-block:: python

    from PIL import Image
    from PILTools import ImageTools

    with Image.open("test.png") as im:
        draw = ImageTools(im)
        draw.rounded_edges(radius=50)

        # write to stdout
        im.save(sys.stdout, "PNG")


Concepts
--------

Colours / Colour names
^^^^^^^^^^^^^^^^^^^^^^

Just like with PIL you can define colours using both integers and tuples.
For more info on how PIL's colour system works refer to the
`PIL documentation <https://pillow.readthedocs.io/en/stable/reference/ImageColor.html>`_.


Functions
---------

.. py:method:: open_online(url, mode="RGBA", size=None, resize_type=3)

    Fetches an image from the internet and then loads it into PIL. (requires `requests <https://github.com/psf/requests>`_ lib)

    :param url: ``str`` - The source URL for the image. HTTP(S) supported, other forms may not work.
    :param mode: ``str`` - The PIL mode to load/convert the image to.
    :param size: ``tuple`` - The size to scale the image to. Leave as None to just keep the original image size.
    :param resize_type: ``int`` - Optional resampling filter for resize if ``size`` defined.

    :returns: ``PIL.Image.Image`` - The loaded image as a PIL Image class.


Draw class
----------

.. py:method:: Draw(im)

    Creates a draw object that can be used to edit the defined image.

    *Note: the image will be modified in place.*

    :param im: ``PIL.Image.Image`` - The image to draw in.

Methods
^^^^^^^

.. py:method:: black_and_white(threshold=150)

    Converts replaces the colour in the image with just black and white without changing the base image mode.

    :param threshold: ``int`` - The threshold for the selection between black and white between 0-255, the higher the threshold the more black the image will be. Defaults to 150.

.. py:method:: grayscale()

    Converts replaces the colour in the image with shades of gray without changing the base image mode.

.. py:method:: greyscale()

    Alias for :py:meth:`~PILTools.ImageTools.Draw.grayscale`

.. py:method:: invert()

    Inverts the colours on the base image (supports transparency).

.. py:method:: rainbow_text(xy, text, fill=None, randomise=False, font=None, align="left", alignY="top", stroke_width=0, stroke_fill=None, embedded_color=None)

    Draws a string of text at the defined position but uses different colours for each letter.

    **Note:** This method is slightly different to vanilla PIL's `PIL.ImageDraw.ImageDraw.text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text>`_ function as anchors are not used.

    :param xy: ``tuple`` - The anchor coordinates of the text.
    :param text: ``str`` - String to be drawn. If it contains any newline characters, the text is passed on to :py:meth:`~PILTools.ImageTools.Draw.rainbow_multiline_text`.
    :param fill: ``list`` - List of colours to use for the rainbow. Will uses the default rainbow colours (:py:data:`PILTools.ImageTools.RAINBOW_DEFAULT`) if none parsed.
    :param randomise: ``bool`` - Make the chosen colours randomised instead of rendering in order. Makes use of `random.choice() <https://docs.python.org/3/library/random.html?highlight=choice#random.choice>`_ for this.
    :param font: ``PIL.ImageFont.ImageFont`` - An `PIL.ImageFont.ImageFont <https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.ImageFont>`_ instance.
    :param align: ``str`` - Determines the relative alignment of the text based off of the x co-ord.
    :param alignY: ``str`` - Determines the relative alignment of the text based off of the y co-ord.
    :param stroke_width: ``int`` - The width of the text stroke.
    :param stroke_fill: ``tuple`` -  Color to use for the text stroke. If not given, will default to the ``fill`` parameter colours.
    :param embedded_color: ``bool`` - Whether to use font embedded color glyphs (COLR or CBDT).

.. py:method:: rainbow_multiline_text(xy, text, fill=None, randomise=False, font=None, spacing=4, align="left", alignY="top", text_align="left", stroke_width=0, stroke_fill=None, embedded_color=None)

    Draws a string of text at the defined position but uses different colours for each letter.

    **Note:** This method is slightly different to vanilla PIL's `PIL.ImageDraw.ImageDraw.multiline_text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.multiline_text>`_ function as anchors are not used.

    :param xy: ``tuple`` - The anchor coordinates of the text.
    :param text: ``str`` - String to be drawn.
    :param fill: ``list`` - List of colours to use for the rainbow. Will uses the default rainbow colours (:py:data:`PILTools.ImageTools.RAINBOW_DEFAULT`) if none parsed.
    :param randomise: ``bool`` - Make the chosen colours randomised instead of rendering in order. Makes use of `random.choice() <https://docs.python.org/3/library/random.html?highlight=choice#random.choice>`_ for this.
    :param font: ``PIL.ImageFont.ImageFont`` - An `PIL.ImageFont.ImageFont <https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.ImageFont>`_ instance.
    :param spacing: ``int`` - The number of pixels between lines.
    :param align: ``str`` - Determines the relative alignment of the text based off of the x co-ord.
    :param alignY: ``str`` - Determines the relative alignment of the text based off of the y co-ord.
    :param text_align: ``str`` - Sets the text alignment similar to the `PIL.ImageDraw.ImageDraw.multiline_text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.multiline_text>`_'s ``align`` argument.
    :param stroke_width: ``int`` - The width of the text stroke.
    :param stroke_fill: ``tuple`` -  Color to use for the text stroke. If not given, will default to the ``fill`` parameter colours.
    :param embedded_color: ``bool`` - Whether to use font embedded color glyphs (COLR or CBDT).

.. py:method:: rounded_edges(radius, fill=None, inverted=False, tl=True, tr=True, bl=True, br=True)

    Adds a rounded edge (corner) effect to the image.

    :param radius: ``int`` - Radius of the edges in pixels.
    :param fill: ``tuple`` - Colour to fill corners with, makes transparent if ``None``. Uses black if image not in transparent friendly mode like ``RGBA``.
    :param inverted: ``bool`` - Determines if the ``fill`` colour covers the cropped corners or the rest of the image.
    :param tl: ``bool`` - Determines whether the ``top left`` corner gets rounded.
    :param tr: ``bool`` - Determines whether the ``top right`` corner gets rounded.
    :param bl: ``bool`` - Determines whether the ``bottom left`` corner gets rounded.
    :param br: ``bool`` - Determines whether the ``bottom right`` corner gets rounded.


Constants
---------

.. data:: RAINBOW_DEFAULT

    A simple list of tuples that define the default colours used in the rainbow text.

    **List of colours:**

    * ``(255, 0, 0)`` - Red
    * ``(255, 106, 0)`` - Orange
    * ``(255, 216, 0)`` - Yellow
    * ``(0, 170, 0)`` - Green
    * ``(0, 148, 255)`` - Blue
    * ``(0, 65, 106)`` - Indigo
    * ``(120, 0, 175)`` - Violet
