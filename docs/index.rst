PIL-Tools
=========

Release v\ |version|.

.. image:: https://pepy.tech/badge/PIL-Tools
    :target: https://pepy.tech/project/PIL-Tools

.. image:: https://img.shields.io/pypi/v/PIL-Tools.svg
    :target: https://pypi.org/project/PIL-Tools/

.. image:: https://img.shields.io/pypi/pyversions/PIL-Tools.svg
    :target: https://pypi.org/project/PIL-Tools/

.. image:: https://img.shields.io/pypi/l/PIL-Tools.svg
    :target: https://pypi.org/project/PIL-Tools/

An extension module for `Pillow <https://github.com/python-pillow/Pillow>`_ to add functions that help simplify some processes.

-------------------

**Simple and easy to learn usage**

.. code-block:: python

    import PIL
    import PILTools

    image = PIL.Image.open("test.png")
    image_draw = PILTools.ImageTools(image)

    # Add a black and white filter to the image with a custom threshold
    image_draw.black_and_white(threshold=100)
    # Curve the corners of the image and replace the removed areas with purple
    image_draw.rounded_edges(radius=50, fill=(175, 0, 200))

    image.show()

**PIL-Tools** uses a PIL styled set of tools to help simplify some effects that you can create with PIL but without the long boring process of having to create them from scratch. It also supports multiple modes of images and makes setting up compatibility between modes easy.


Overview
--------
.. toctree::
   :maxdepth: 2

   reference/index.rst
   releasenotes/index.rst


Installation
------------

Install with pip
^^^^^^^^^^^^^^^^
::

    $ pip install PIL-Tools

Update with pip
^^^^^^^^^^^^^^^
::

    $ pip install PIL-Tools --upgrade

Install from source
^^^^^^^^^^^^^^^^^^^
::

    $ python setup.py install


Support
-------
If you have any problems with PIL-Tools please let me know via `the GitHub issue tracker <https://github.com/stshrewsburyDev/PIL-Tools/issues>`_.


Some useful links
-----------------

- Issue Tracker: https://github.com/stshrewsburyDev/PIL-Tools/issues
- Source Code: https://github.com/stshrewsburyDev/PIL-Tools


License
-------

The project is licensed under the MIT license.