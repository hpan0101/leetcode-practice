import pytest
from p0001_two_sum import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example1(solution):
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example2(solution):
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]


def test_example3(solution):
    assert solution.twoSum([3, 3], 6) == [0, 1]
