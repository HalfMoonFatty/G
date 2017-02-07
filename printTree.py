'''
Problem: 

给一个数据结构
class Purchase(object): 
    def __init__(self, id, val, previous):
        self.id = id
        self.val = val
        self.previous = previous # 每个节点指向自己的parent



输入是 a List of Purchase, 打印每个节点的及其子节点的value。

Example：
              Node1, 1
               /     \      
      Node2, 2      Node3, 4
          /
Node4, 1      


Output: node1, 8  Node 2, 3  Node 3,4 Node4,1

Reference: http://www.1point3acres.com/bbs/thread-211354-1-1.html
'''

# Solution: 可以先生成一个purchase 和 in-degree 的map， 然后把leave 节点放入一个queue里，然后更新这个map， 找到新的leave

import collections
class Purchase(object): 
    def __init__(self, id, val, previous):
        self.id = id
        self.val = val
        self.previous = previous


class Solution(object):
    def printTree(self, purchase):

        indegree = collections.defaultdict(int)
        for p in purchase:
            if p.previous: 
                indegree[p.previous.id] += 1

        ret = []

        leaves = [p for p in purchase if indegree[p.id] == 0]
        q = collections.deque(leaves)
        while len(q):
            node = q.popleft()
            ret.append((node.id, node.val))
            if node.previous:
                node.previous.val += node.val
                indegree[node.previous.id] -= 1
                if indegree[node.previous.id] == 0:
                    q.append(node.previous)

        return ret
    
