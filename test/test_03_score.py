from challenges.score_03 import Solution
import pytest

@pytest.mark.parametrize("nums,result", [
    ([1,3,2], 2),
    ([4,9,7,1,3], 7)
])
def test_03_score(nums, result):
    s = Solution()
    assert s.get_runner_score(nums) == result
    