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
