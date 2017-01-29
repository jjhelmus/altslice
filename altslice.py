
class UniformSlicer(object):

    def __init__(self, start, step):
        self._start = start
        self._step = step

    def _transform_index(self, index):
        return int((index - self._start) // (self._step))

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


class CategoricalSlicer(object):

    def __init__(self, categories):
        if hasattr(categories, 'index'):
            self._categories = categories
        else:
            self._categories = tuple(catagories)

    def _transform_index(self, index):
        return self._categories.index(index)

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
