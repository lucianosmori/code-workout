class Solution:
    def get_runner_score(self, scores):
        scores = list(set(scores))        
        scores.sort()
        return scores[-2]


if __name__ == '__main__':
    #n = int(input().split())
    n = [1,3,2]
    #arr = map(int, input().split())
    s = Solution()
    print(s.get_runner_score(n))