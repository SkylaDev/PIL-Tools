The ImageTools class
====================

The ImageDraw class provides simple 2D effects for
`Image <https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image>`_
objects, this includes some image filters, custom cropping/filling and more.


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

.. py:method:: ImageTools(im)

    Creates a draw object that can be used to edit the defined image.

    *Note: the image will be modified in place.*

    :param im: The image to draw in.

Methods
-------

.. py:method:: ImageDraw.black_and_white(threshold=150)

    Converts replaces the colour in the image with just black and white without changing the base image mode.

    :param threshold: The threshold for the selection between black and white, the higher the threshold the more black the image will be. (default 150)


.. py:method:: ImageDraw.grayscale()

    Converts replaces the colour in the image with shades of gray without changing the base image mode.


.. py:method:: ImageDraw.invert()

    Inverts the colours on the base image (supports transparency).


.. py:method:: ImageDraw.rounded_edges(radius, fill=None, inverted=False, tl=True, tr=True, bl=True, br=True)

    Adds a rounded edge effect to the image.

    :param radius: Radius of the edges in pixels.
    :param fill: Colour to fill corners with, makes transparent if None (black if image not in transparent friendly mode like RGBA.)
    :param inverted: Determines if the ``fill`` colour covers the cropped corners or the rest of the image.
    :param tl: Determines whether the top left corner is rounded.
    :param tr: Determines whether the top right corner is rounded.
    :param bl: Determines whether the bottom left corner is rounded.
    :param br: Determines whether the bottom right corner is rounded.
