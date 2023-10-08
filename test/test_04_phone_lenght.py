from challenges.phone_number_lenght_04 import Solution

import pytest

@pytest.mark.parametrize("nums,result", [
    (8991231235, "YES"),
    (1991231235, "NO"),
    ("9991231235", "YES"),
    ("8F54698745", "NO"),

])
def test_03_score(nums, result):
    s = Solution()
    assert s.validate_numbers(nums) == result
