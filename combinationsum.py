def combinationSum(self, candidates : List[int], arget: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total ==
