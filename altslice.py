

class CategoricalSlicer(object):

    def __init__(self, categories):
        if hasattr(categories, 'index'):
            self._categories = categories
        else:
            self._categories = tuple(catagories)

    def __getitem__(self, x):
        """ Return an int/slice. """
        if isinstance(x, slice):
            print(x)
            start = stop = step = None
            if x.start is not None:
                start = self._categories.index(x.start)
            if x.stop is not None:
                stop = self._categories.index(x.stop)
            step = x.step  # step is not transformed
            return slice(start, stop, step)
        else:  # single element
            return self._categories.index(x)

    def __call__(self, *args):
        return self.__getitem__(slice(*args))
