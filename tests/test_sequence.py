from altslice import SequenceSlicer


def test_categorical():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sequence = [0.1, 0.5, 1.2, 2.4, 2.8, 3.6, 4.6, 5.9, 7.7, 9.9]
    # data        1    2    3    4    5    6    7    8    9   10
    slicer = SequenceSlicer(sequence)

    # single index
    assert data[slicer[0.1]] == 1
    assert data[slicer[2.8]] == 5

    # start:end
    assert data[slicer[0.1:2.3]] == [1, 2, 3]
    assert data[slicer[1.2:6.]] == [3, 4, 5, 6, 7, 8]

    # :end
    assert data[slicer[:1.0]] == [1, 2]

    # start:
    assert data[slicer[3.2:]] == [6, 7, 8, 9, 10]

    # as a slice-like object
    assert data[slicer(1.0)] == [1, 2]
    assert data[slicer(-0.2, 2.0)] == [1, 2, 3]
    assert data[slicer(1, 6)] == [3, 4, 5, 6, 7, 8]
