def maxRscKnode(root, k):

    def maxRsc(root, k)
       if not root: 
            return 0
        if not root.left and root.right:
            dp[root][1] = root.val
        else:
            maxVal = 0
            for i in range(k): # i from [0, k-1]
                if dp[root.left][i]:
                    leftVal = dp[root.left][i]
                else:
                    leftVal = maxRsc(root, i)
                if dp[root.right][k-1-i]:
                    rightVal = dp[root.right][k-1-i]
                else:
                    rightVal = maxRsc(root, k-1-i)
                maxVal = max(maxVal, (leftVal + rightVal) + root.val)
                dp[root][k] = maxVal
        return maxVal

    dp = collections.defaultdict(list)
