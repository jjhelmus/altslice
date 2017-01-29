
from altslice import CategoricalSlicer


def test_categorical():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    catagories = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    slicer = CategoricalSlicer(catagories)

    # single index
    assert data[slicer['a']] == 1
    assert data[slicer['e']] == 5

    # start:end
    assert data[slicer['a':'d']] == [1, 2, 3]
    assert data[slicer['c':'i']] == [3, 4, 5, 6, 7, 8]

    # :end
    assert data[slicer[:'c']] == [1, 2]

    # start:
    assert data[slicer['f':]] == [6, 7, 8, 9, 10]

    # as a slice-like object
    assert data[slicer('c')] == [1, 2]
    assert data[slicer('a', 'd')] == [1, 2, 3]
    assert data[slicer('c', 'i')] == [3, 4, 5, 6, 7, 8]
