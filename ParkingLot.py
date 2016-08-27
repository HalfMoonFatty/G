'''
Problem: Rearrange an array using swap with 0. 

You have two arrays src, tgt, containing two permutations of the numbers 0..n-1. You would like to rearrange src so that it equals tgt. 
The only allowed operations is “swap a number with 0”, e.g. {1,0,2,3} -> {1,3,2,0} (“swap 3 with 0”). 
Write a program that prints to stdout the list of required operations. 

Practical application: 

Imagine you have a parking place with n slots and n-1 cars numbered from 1..n-1. The free slot is represented by 0 in the problem. 
If you want to rearrange the cars, you can only move one car at a time into the empty slot, which is equivalent to “swap a number with 0”. 

Example: 
src={1,0,2,3}; tgt={0,2,3,1};

'''


'''
Solution:
The question does not require the minimum swap number. 
So, an easy way to do is, find the index of first does not match (except ZERO), 
then swap ZERO with it, then swap ZERO with the tgt value of that index. 
Just loop for all positions. Then, it is done. 
eg. {0, 1, 2} -> {0, 2, 1} 
first does not match index is 1, and tgt value is 2. 
So, {0, 1, 2}-> {1, 0, 2}->{1, 2, 0} 

If it require the minimum swap number, then, shortest path algorithm will resolve it. 
Every permutation is one node, and all possible links are just a swap of ZERO. 
For performance improvement, A* can be used. 
So, never swap ZERO with any value that matched already. 
And it is better to generate nodes in run time.

https://www.careercup.com/question?id=5700226908160000

'''


def recoverArr(src,tar):

	ind = {item:i for i, item in enumerate(tar)}

	for i in range(len(tar)):
		if tar[i] == src[i]:
			continue

		# swap current with 0
		tar[i],tar[ind[0]] = tar[ind[0]],tar[i]
		ind[0],ind[tar[i]] = i,ind[0]

		# swap 0 with the correct number
		tar[i],tar[ind[src[i]]] = tar[ind[src[i]]],tar[i]
		ind[0],ind[src[i]] = ind[src[i]],i


	return 

src = [0,1,2,3]
tar = [2,0,3,1]
recoverArr(src,tar)
print tar
