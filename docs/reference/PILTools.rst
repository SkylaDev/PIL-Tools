The PILTools module
===================

The base PILTools module includes a few utility functions that can help with opening
and handling images from PIL.


Example: Open an image from the internet into PIL
-------------------------------------------------

.. code-block:: python

    import PILTools

    image = PILTools.open_image(url="http://example.com/image.png")
    # Note: http://example.com/image.png isn't actually an image it is just there for example purposes


Functions
---------

.. py:method:: open_online(url, mode="RGBA", size=None, resize_type=3)

    Fetches an image from the internet and then loads it into PIL. (requires `requests <https://github.com/psf/requests>`_ lib)

    **Note:** For a async version of this function refer to :py:meth:`async_open_online()`

    :param str url: The source URL for the image. HTTP(S) supported, other forms may not work.
    :param str mode: The PIL mode to load/convert the image to.
    :param tuple size: The size to scale the image to. Leave as None to just keep the original image size.
    :param int resize_type: Optional resampling filter for resize if ``size`` defined.

    :returns: The loaded image as a PIL Image class.
    :rtype: PIL.Image.Image

    :raises: :py:exc:`InvalidImageURL()` if the module cannot read any image data from the given URL.

.. py:method:: async_open_online(url, mode="RGBA", size=None, resize_type=3)

    Asynchronously fetches an image from the internet and then loads it into PIL. (requires `aiohttp <https://github.com/aio-libs/aiohttp>`_ lib)

    **Note:** For a non-async version of this function refer to :py:meth:`open_online()`

    :async:
    :param str url: The source URL for the image. HTTP(S) supported, other forms may not work.
    :param str mode: The PIL mode to load/convert the image to.
    :param tuple size: The size to scale the image to. Leave as None to just keep the original image size.
    :param int resize_type: Optional resampling filter for resize if ``size`` defined.

    :returns: The loaded image as a PIL Image class.
    :rtype: PIL.Image.Image

    :raises: :py:exc:`InvalidImageURL()` if the module cannot read any image data from the given URL.
