
import abc
import bisect


class Slicer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def _transform_index(self, x):
        pass

    def __getitem__(self, x):
        """ Return an int/slice. """
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
        return self.__getitem__(slice(*args))


class SequenceSlicer(Slicer):

    def __init__(self, sequence):
        self._sequence = sequence

    def _transform_index(self, index):
        return bisect.bisect_left(self._sequence, index)


class UniformSlicer(Slicer):

    def __init__(self, start, step):
        self._start = start
        self._step = step

    def _transform_index(self, index):
        return int((index - self._start) // (self._step))


class OneBasedSlicer(UniformSlicer):

    def __init__(self):
        self._start = 1
        self._step = 1

    def _transform_index(self, x):
        if not isinstance(x, int):
            raise TypeError("indices must be integers not " + str(type(x)))
        elif x == 0:
            raise IndexError("0 not allowed in one based indexinng")
        elif x < 0:
            return x
        else:
            return super(OneBasedSlicer, self)._transform_index(x)


class CategoricalSlicer(Slicer):

    def __init__(self, categories):
        if hasattr(categories, 'index'):
            self._categories = categories
        else:
            self._categories = tuple(catagories)

    def _transform_index(self, index):
        return self._categories.index(index)
