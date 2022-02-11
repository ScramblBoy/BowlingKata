from BowlingKata import functional_approach


def test_are_all_frames_valid():
    assert not functional_approach.are_all_frames_valid([10, 0, 15, 2, 3, 4, 5, 6])
    assert not functional_approach.are_all_frames_valid([10, 10])
    assert [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]


def test_is_valid_sequence():
    assert not functional_approach.is_valid_sequence([10, 0])
    assert not functional_approach.is_valid_sequence([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1])


def test_calculate_score():
    assert functional_approach.calculate_score([9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]) == 90
    assert functional_approach.calculate_score([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
    assert functional_approach.calculate_score(
        [10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 10]) == 300
