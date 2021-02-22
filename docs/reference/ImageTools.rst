The ImageTools module
=====================

The ImageDraw module provides simple 2D effects for
`Image <https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image>`_
objects, this includes some image filters, custom cropping/filling and more.


Example: Round off corners of an image
--------------------------------------

.. code-block:: python

    from PIL import Image
    from PILTools import ImageTools

    with Image.open("test.png") as im:
        draw = ImageTools.Draw(im)
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


Draw class
----------

.. py:class:: Draw(im)

    Creates a draw object that can be used to edit the defined image.

    **Note:** the image will be modified in place.

    :param PIL.Image.Image im: The image to draw in.

Methods
^^^^^^^

.. py:method:: Draw.black_and_white(threshold=150)

    Converts replaces the colour in the image with just black and white without changing the base image mode.

    *New in version 1.0: Supports alpha transparency*

    :param int threshold: The threshold for the selection between black and white between 0-255, the higher the threshold the more black the image will be. Defaults to 150.

    :raises: :py:exc:`InvalidThreshold()` if the threshold provided was invalid (not in 0-255).

.. py:method:: Draw.blue_screen(r_threshold: int=80, g_threshold: int=80, b_threshold: int=100)

    Attempts to remove blue from an image based on the thresholds set.

    :param int r_threshold: The red threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.
    :param int g_threshold: The green threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.
    :param int b_threshold: The blue threshold to use between 0-255, anything **below** this threshold will be kept. Defaults to 100.

    :raises: :py:exc:`InvalidThreshold()` if one of the thresholds provided were invalid (not in 0-255).

.. py:method:: Draw.grayscale()

    Converts replaces the colour in the image with shades of gray without changing the base image mode.

    *New in version 1.0: Supports alpha transparency*

.. py:method:: Draw.greyscale()

    Alias for :py:meth:`Draw.grayscale()`

    *New in version 1.0: Supports alpha transparency*

.. py:method:: Draw.green_screen(r_threshold: int=80, g_threshold: int=100, b_threshold: int=80)

    Attempts to remove green from an image based on the thresholds set.

    :param int r_threshold: The red threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.
    :param int g_threshold: The green threshold to use between 0-255, anything **below** this threshold will be kept. Defaults to 100.
    :param int b_threshold: The blue threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.

    :raises: :py:exc:`InvalidThreshold()` if one of the thresholds provided were invalid (not in 0-255).

.. py:method:: Draw.invert()

    Inverts the colours on the base image (supports transparency).

.. py:method:: Draw.rainbow_text(xy, text, fill=None, randomise=False, font=None, align="left", alignY="top", stroke_width=0, stroke_fill=None, embedded_color=None)

    Draws a string of text at the defined position but uses different colours for each letter.

    **Note:** This method is slightly different to vanilla PIL's `PIL.ImageDraw.ImageDraw.text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text>`_ function as anchors are not used.

    :param tuple xy: The anchor coordinates of the text.
    :param str text: String to be drawn. If it contains any newline characters, the text is passed on to :py:meth:`Draw.rainbow_multiline_text()`.
    :param list fill: List of colours to use for the rainbow. Will uses the default rainbow colours (:py:data:`RAINBOW_DEFAULT`) if none parsed.
    :param bool randomise: Make the chosen colours randomised instead of rendering in order. Makes use of `random.choice() <https://docs.python.org/3/library/random.html?highlight=choice#random.choice>`_ for this.
    :param PIL.ImageFont.ImageFont font: An `PIL.ImageFont.ImageFont <https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.ImageFont>`_ instance.
    :param str align: Determines the relative alignment of the text based off of the x co-ord.
    :param str alignY: Determines the relative alignment of the text based off of the y co-ord.
    :param int stroke_width: The width of the text stroke.
    :param tuple stroke_fill: Color to use for the text stroke. If not given, will default to the ``fill`` parameter colours.
    :param bool embedded_color: Whether to use font embedded color glyphs (COLR or CBDT).

.. py:method:: Draw.rainbow_multiline_text(xy, text, fill=None, randomise=False, font=None, spacing=4, align="left", alignY="top", text_align="left", stroke_width=0, stroke_fill=None, embedded_color=None)

    Draws a string of text at the defined position but uses different colours for each letter.

    **Note:** This method is slightly different to vanilla PIL's `PIL.ImageDraw.ImageDraw.multiline_text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.multiline_text>`_ function as anchors are not used.

    :param tuple xy: The anchor coordinates of the text.
    :param str text: String to be drawn.
    :param list fill: List of colours to use for the rainbow. Will uses the default rainbow colours (:py:data:`RAINBOW_DEFAULT`) if none parsed.
    :param bool randomise: Make the chosen colours randomised instead of rendering in order. Makes use of `random.choice() <https://docs.python.org/3/library/random.html?highlight=choice#random.choice>`_ for this.
    :param PIL.ImageFont.ImageFont font: An `PIL.ImageFont.ImageFont <https://pillow.readthedocs.io/en/stable/reference/ImageFont.html#PIL.ImageFont.ImageFont>`_ instance.
    :param int spacing: The number of pixels between lines.
    :param str align: Determines the relative alignment of the text based off of the x co-ord.
    :param str alignY: - Determines the relative alignment of the text based off of the y co-ord.
    :param str text_align: Sets the text alignment similar to the `PIL.ImageDraw.ImageDraw.multiline_text() <https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.multiline_text>`_'s ``align`` argument.
    :param int stroke_width: The width of the text stroke.
    :param tuple stroke_fill: Color to use for the text stroke. If not given, will default to the ``fill`` parameter colours.
    :param bool embedded_color: Whether to use font embedded color glyphs (COLR or CBDT).

.. py:method:: Draw.red_screen(r_threshold: int=100, g_threshold: int=80, b_threshold: int=80)

    Attempts to remove red from an image based on the thresholds set.

    :param int r_threshold: The red threshold to use between 0-255, anything **below** this threshold will be kept. Defaults to 100.
    :param int g_threshold: The green threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.
    :param int b_threshold: The blue threshold to use between 0-255, anything **above** this threshold will be kept. Defaults to 80.

    :raises: :py:exc:`InvalidThreshold()` if one of the thresholds provided were invalid (not in 0-255).

.. py:method:: rounded_edges(radius, fill=None, inverted=False, tl=True, tr=True, bl=True, br=True)

    Adds a rounded edge (corner) effect to the image.

    :param int radius: Radius of the edges in pixels.
    :param tuple fill: Colour to fill corners with, makes transparent if ``None``. Uses black if image not in transparent friendly mode like ``RGBA``.
    :param bool inverted: Determines if the ``fill`` colour covers the cropped corners or the rest of the image.
    :param bool tl: Determines whether the ``top left`` corner gets rounded.
    :param bool tr: Determines whether the ``top right`` corner gets rounded.
    :param bool bl: Determines whether the ``bottom left`` corner gets rounded.
    :param bool br: Determines whether the ``bottom right`` corner gets rounded.


Constants
---------

.. py:data:: RAINBOW_DEFAULT

    A simple list of tuples that define the default colours used in the rainbow text.

    **List of colours:**

    * ``(255, 0, 0)`` - Red
    * ``(255, 106, 0)`` - Orange
    * ``(255, 216, 0)`` - Yellow
    * ``(0, 170, 0)`` - Green
    * ``(0, 148, 255)`` - Blue
    * ``(0, 65, 106)`` - Indigo
    * ``(120, 0, 175)`` - Violet

    :type: list
