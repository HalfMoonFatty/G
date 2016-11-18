'''
给一个String和一个字典，找字典里面长度最长的能由String里面删去某些字符后组成的单词 
比如S = abpcplea， Dict = {ale, apple, monkey, plea}, 就返回apple 
'''

# Time : O(n!)
# Space: O(n!)

def maxLengthStr(s, Dict):
    maxLen = -1
    ret = None
    if not s or s in Dict: 
        return s
    else:
        for i in range(len(s)):
            cur = maxLengthStr(s[:i]+s[i+1:], Dict)
            if cur and len(cur) > maxLen:
                maxLen = len(cur)
                ret = cur
    return ret


Dict = {"ale", "apple", "monkey", "plea"}
S = "abpcplea"
print maxLengthStr(S, Dict)
