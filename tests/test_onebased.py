from altslice import OneBasedSlicer

import pytest


def test_uniform():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slicer = OneBasedSlicer()

    # single index
    assert data[slicer[1]] == 1
    assert data[slicer[5]] == 5

    # start:end
    assert data[slicer[1:4]] == [1, 2, 3]
    assert data[slicer[3:9]] == [3, 4, 5, 6, 7, 8]

    # :end
    assert data[slicer[:3]] == [1, 2]

    # start:
    assert data[slicer[6:]] == [6, 7, 8, 9, 10]

    # as a slice-like object
    assert data[slicer(3)] == [1, 2]
    assert data[slicer(1, 4)] == [1, 2, 3]
    assert data[slicer(3, 9)] == [3, 4, 5, 6, 7, 8]

    # non-intergers should raise an exceptions
    with pytest.raises(TypeError):
        data[slicer[3.5]]

    # zero should raise an exception
    with pytest.raises(IndexError):
        data[slicer[0]]

    # negative intergers
    assert data[slicer[5:-1]] == [5, 6, 7, 8, 9]
