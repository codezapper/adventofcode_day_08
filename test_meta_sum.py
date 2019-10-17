from unittest import mock
from unittest.mock import patch, mock_open

from meta_sum import extract_metadata, get_and_remove_node, main, get_numbers_from_file


def test_get_and_remove_node():
    cases = [
        {
            "input": {"numbers": [0, 1, 2], "start_index": 0},
            "expected_node": [0, 1, 2],
            "expected_numbers": [],
        },
        {
            "input": {
                "numbers": [1, 1, 2, 0, 2, 6, 7, 8, 9],
                "start_index": 3,
            },
            "expected_node": [0, 2, 6, 7],
            "expected_numbers": [1, 1, 2, 8, 9],
        },
    ]

    for case in cases:
        node = get_and_remove_node(**case["input"])
        assert node == case["expected_node"]
        assert case["input"]["numbers"] == case["expected_numbers"]


def test_extract_metadata():
    cases = [
        {
            "input": {"numbers": [0, 1, 2], "start_index": 0},
            "expected_metadata": [2],
            "expected_numbers": [],
        },
        {
            "input": {
                "numbers": [1, 1, 2, 0, 2, 6, 7, 8, 9],
                "start_index": 3,
            },
            "expected_metadata": [2, 6, 7],
            "expected_numbers": [1, 1, 2, 8, 9],
        },
        {
            "input": {
                "numbers": [
                    2, 3, 0, 3, 10, 11, 12, 1,
                    1, 0, 1, 99, 2, 1, 1, 2,
                ],
                "start_index": 0,
            },
            "expected_metadata": [2, 6, 7, 10, 11, 12, 99, 2, 1, 1, 2],
            "expected_numbers": [],
        },
    ]

    for case in cases:
        metadata = extract_metadata(**case["input"])
        assert metadata == case["expected_metadata"]
        assert case["input"]["numbers"] == case["expected_numbers"]


@mock.patch("meta_sum.extract_metadata")
@mock.patch("meta_sum.get_numbers_from_file")
def test_main(get_numbers_mock, extract_mock):
    get_numbers_mock.return_value = None
    main()
    assert not extract_mock.called

    get_numbers_mock.return_value = [1, 2, 3]
    main()
    extract_mock.assert_called_once_with([1, 2, 3])


def test_get_numbers_from_file():
    with patch("builtins.open", mock_open(read_data="1 2 3")):
        numbers = get_numbers_from_file("fake_file.txt")
        assert numbers == [1, 2, 3]

    with patch("builtins.open", mock_open()):
        numbers = get_numbers_from_file("fake_file.txt")
        assert numbers == []


