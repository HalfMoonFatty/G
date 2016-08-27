'''
Problem:
首先给一个字典，比如：{apple, people,...} 再给一个misspelling word，比如：adple，返回它的正确拼写，即 apple 
还知道一个限制条件，misspelling word只跟原单词有一个字母的区别。如果输入是addle，返回null。如果字数不同，也返回null 
'''

import string
def isMissSpelling(s,d):
	for i in range(len(s)):
		for char in string.ascii_lowercase:
			if char == s[i]:
				continue
			if s[:i]+char+s[i+1:] in d:
				return True
	return False


test = 'abple'
d = set(['apple'])
print isMissSpelling(test,d)


'''
改进版本：最多有两个不一样
'''
import string
def isMissSpelling(ss,start,d,k):
	if start == len(ss):
		return ss in d and k>=0

	for i in range(start,len(ss)):
		for char in string.ascii_lowercase:
			if ss[i] == char:
				if isMissSpelling(ss[:],i+1,d,k): return True
			if isMissSpelling(ss[:i]+char+ss[i+1:],i+1,d,k-1): return True
			else: continue
	return False



test = 'heljo'
d = set(['hello'])
k = 2
print isMissSpelling(test,0,d,k)
