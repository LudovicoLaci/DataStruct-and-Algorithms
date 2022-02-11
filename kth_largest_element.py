#!/usr/bin/python3

"""
Given an array of integers arr and an integer k, find the kth largest element.
"""

# First solution: remove the max elem k-1 times.
def kth_largest(arr, k):
	for i in range(k-1):
		arr.remove(max(arr))
	return max(arr)
# T(n,k) = (k-1) * 2n + n = 2kn - n = O(kn).
# S(n,k) = O(1).


# Second solution: Sorting ==> largest at the end and sorted.
def kth_largest2(arr, k):
	n = len(arr)
	arr.sort()				# T(n) = O(nlogn)
	return arr[n-k]			# T(n) = O(1)
# T(n,k) = O(nlogn) + O(1) = O(nlogn)


# Third solution: Priority queue.
import heapq		# Implemented with min heap and not max heap ==> * (-1).

def kth_largest3(arr, k):
	arr = [-elem for elem in arr]	# T(n) = O(n)
	heapq.heapify(arr)				# T(n) = O(n)
	for i in range(k-1):			# T(k,n) = O(k-1) + O(logn)
		heapq.heappop(arr)
	return -heap.heappop(arr)		# T(n) = O(logn)
# T(n,k) = 2n + (k-1) * logn + logn
# T(n,k) = 2n + klogn = O(n + klogn)
# S(n,k) = O(n)
