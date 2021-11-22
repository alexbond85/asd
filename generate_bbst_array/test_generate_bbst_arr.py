from gen_bbst_arr import GenerateBBSTArray


def test_generate_bbst_array_empty():
    input = []
    assert GenerateBBSTArray(input) == []


def test_generate_bbst_array_one_element():
    input = [0]
    assert GenerateBBSTArray(input) == [0]


def test_generate_bbst_array_three_elements():
    input = [0, 1, 2]
    assert GenerateBBSTArray(input) == [1, 0, 2]


def test_generate_bbst_array_seven_elements():
    input = [0, 1, 2, 3, 4, 5, 6]
    assert GenerateBBSTArray(input) == [3, 1, 5, 0, 2, 4, 6]


def test_generate_bbst_array_fifteen_elements():
    input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    output = [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]
    assert GenerateBBSTArray(input) == output
