altslice : Index different
==========================

The altslice package provides a number of **Slicer** classes which can be used
to index and slice sequences using alternative indexing. For example:

.. code:: python

    from altslice import CategoricalSlicer

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 200, 250, 300, 333, 400]

    slicer = CategoricalSlicer(months)

    # sales total from January
    sales[slicer['Jan']]

    # sales from Febuary until May
    sales[slicer['Jan':'May']]

Slicers
-------

The following Slicers are provided in the library:

* CategoricalSlicer : Index using discrete categories.
* UniformSlicer : Index using evenly spaced numbers with a specific interval.
* SeqeuenceSlicer : Index using a sorted sequence of numbers.
* OneBasedSlicer : One-based indexing.

Install
-------

altslice can be installed using pip:

.. code::

    pip install altslice

Testing
-------

altslice uses pytest for testing.  The test suite can be executed using
**py.test**.

One-based indexing
------------------

If desired the list container can be adjusted to use one-based indexing:

.. code:: python

   from altslice import OneBasedSlicer

   slicer = OneBasedSlicer()

   class list(list):
       def __getitem__(self, x):
           return super(list, self).__getitem__(slicer[x])

This adjustment is not recommended.
