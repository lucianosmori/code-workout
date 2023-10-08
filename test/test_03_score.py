from challenges.score_03 import Solution
import pytest

@pytest.mark.parametrize("list,result", [
    ([1,3,2], 2)
])
def test_03_score(list, result):
    s = Solution()
    assert s.get_runner_score(list) == result
    