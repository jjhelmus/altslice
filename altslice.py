"""
altslice : Index different

Classes of alternative indexing of Python sequences.

"""

import bisect

__version__ = "0.1.0"


class Slicer(object):
    """
    Base class for all Slicers

    To subclass, a _transform_index method must be defined.  This method
    transforms values from the new index scheme to Python's normal indexing
    scheme.
    """

    def _transform_index(self, x):
        raise NotImplementedError

    def __getitem__(self, x):
        """ Return an int or slice in Python's natural indexing scheme. """
        if isinstance(x, slice):
            start = stop = step = None
            if x.start is not None:
                start = self._transform_index(x.start)
            if x.stop is not None:
                stop = self._transform_index(x.stop)
            step = x.step  # step is not transformed
            return slice(start, stop, step)
        else:  # single element
            return self._transform_index(x)

    def __call__(self, *args):
        """ stop or start, stop, [step]. """
        return self.__getitem__(slice(*args))


class SequenceSlicer(Slicer):
    """ Slice using indices of a asending sequence.

    Create indices and slices based on an asending sequence of values.
    Indexing and slicing is done to the left of the indices provided.

    """

    def __init__(self, sequence):
        self._sequence = sequence

    def _transform_index(self, index):
        return bisect.bisect_left(self._sequence, index)


class UniformSlicer(Slicer):
    """ Slice using indices of an evenly spaced interval.

    Create indices and slices based upon an given evenly spaced interval
    starting at a given value.
    Indexing and slicing is done to the left of the indices provided.

    """

    def __init__(self, start, step):
        self._start = start
        self._step = step

    def _transform_index(self, index):
        return int((index - self._start) // (self._step))


class OneBasedSlicer(UniformSlicer):
    """ Slice using one-based indexing.

    Create indices and slices where the first value is index 1.
    None integer indices or slice components will raise a TypeError.
    """

    def __init__(self):
        self._start = 1
        self._step = 1

    def _transform_index(self, x):
        if not isinstance(x, int):
            raise TypeError("indices must be integers not " + str(type(x)))
        elif x == 0:
            raise IndexError("0 not allowed in one-based indexing")
        elif x < 0:
            return x
        else:
            return super(OneBasedSlicer, self)._transform_index(x)


class CategoricalSlicer(Slicer):
    """ Slice using given categories.

    Create indices and slices using the provides sequence of categories.
    Indices and slice components not found in the provide categories will raise
    a ValueError.

    """

    def __init__(self, categories):
        if hasattr(categories, 'index'):
            self._categories = categories
        else:
            self._categories = tuple(catagories)

    def _transform_index(self, index):
        return self._categories.index(index)
