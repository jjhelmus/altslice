
from altslice import UniformSlicer


def test_uniform():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #       1  11 21 31 41 51 61 71 81 91
    slicer = UniformSlicer(start=1, step=10)

    # single index
    assert data[slicer[1]] == 1
    assert data[slicer[41]] == 5

    # start:end
    assert data[slicer[1:31]] == [1, 2, 3]
    assert data[slicer[21:81]] == [3, 4, 5, 6, 7, 8]

    # :end
    assert data[slicer[:21]] == [1, 2]

    # start:
    assert data[slicer[51:]] == [6, 7, 8, 9, 10]

    # as a slice-like object
    assert data[slicer(21)] == [1, 2]
    assert data[slicer(1, 31)] == [1, 2, 3]
    assert data[slicer(21, 81)] == [3, 4, 5, 6, 7, 8]
