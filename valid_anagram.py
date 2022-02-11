#!/usr/bin/python3

"""
Given two strings s1 and s2, check if they're anagrams. Two strings are anagrams
if they're made of the same characters with the same frequencies.
"""

def are_anagrams(s1, s2):
	if len(s1) != len(s2):
		return False
	freq1 = {}					# S(n) = O(n)
	freq2 = {}					# S(n) = O(n)
	for ch in s1:				# T(n) = O(n)
		if ch in freq1:
			freq1[ch] += 1
		else:
			freq1[ch] = 1
	for ch in s2:				# T(n) = O(n)
		if ch in freq2:
			freq2[ch] += 1
		else:
			freq2[ch] = 1
	for key in freq1:			# T(n) = O(n)
		if key not in freq2 or freq1[key] != freq2[key]:
			return False
	return True
# T(n) = O(n) + O(n) + O(n) = O(n)
# S(n) = O(n) + O(n) = O(n)

"""
In python counter() method in collections module build the table of occurencies.
"""

from collections import Counter

def are_anagrams2(s1, s2):
	if len(s1) != len(s2):
		return False
	return Counter(s1) == Counter(s2)

"""
Two anagrams have the same sorted string.
"""

def are_anagrams3(s1, s2):
	if len(s1) != len(s2):
		return False
	return sorted(s1) == sorted(s2)
# T(n) = O(nlogn) + O(nlogn) + n = O(nlogn)
# S(n) = 2n = O(n)
