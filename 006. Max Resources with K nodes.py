'''
Problem:

       A 1
    /       \ 
   B 3       C 2
 /  \       /
D 6  E 9   F 8

e.g k = 3

'''

'''
Solution 1: dp

┏━━━┳━━━┳━━━┳━━━┳━━━┓
┃   ┃ 0  ┃ 1 ┃ 2 ┃ 3 ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ D ┃ 0  ┃ 6 ┃   ┃ ? ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ E ┃ 0  ┃ 9 ┃   ┃ ? ┃   
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ F ┃ 0  ┃ 8 ┃   ┃ ? ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ B ┃ 0  ┃ 3 ┃   ┃ ? ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ C ┃ 0  ┃ 2 ┃   ┃ ? ┃
┣━━━╋━━━╋━━━╋━━━╋━━━┫
┃ A ┃ 0  ┃ 1 ┃   ┃ ? ┃
┗━━━┻━━━┻━━━┻━━━┻━━━┛

define: dp[i][j] = max(dp[i.left][x] + dp[j.left][j-1-x]) for x in range [0,k-1]

'''



def maxRscKnode(root, k):

    def traverse(root, nodes):
        if not root:
            return
        else:
            traverse(root.left, nodes)
            traverse(root.right, nodes)
            nodes.append(root)
            return


    nodes = []
    traverse(root, nodes)

    dp = [[0] * (k+1) for n in range len(nodes)]
    for n in nodes:
        dp[n][1] = n.val

    # dp[i][j] = max(dp[i.left][x] + dp[j.left][j-1-x]) for j in range [0,j-1]
    for i in nodes:  # take any node as root
        for j in range(2,k+1): # j increases from 2 to k
            maxVal = -sys.maxint-1
            for x in range(1,j-1): 
                leftVal = dp[i.left][x]
                rightVal = dp[i.right][j-1-x]
                maxVal = max(maxVal, leftVal + rightVal + i.val)
            dp[i][j] = max(dp[i][j], maxVal)

    # loop through dp[n][k]
    maxVal = - sys.maxint -1
    for i in nodes:
        maxVal = max(maxVal, dp[i][-1]

    return maxVal




'''
Solution 2: Cache

'''

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
