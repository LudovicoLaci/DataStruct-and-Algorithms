#!/usr/bin/python3

class HashMap(object):
	def __init__(self):
		self.hashmap = [[] for i in range(256)]

	def insert(self, key, value):
		hash_key = hash(key) % len(self.hashmap)
		key_exists = False
		bucket = self.hashmap[hash_key]
		for i, kv in enumerate(bucket):
			k, v = kv
			if key == k:
				key_exists = True
				break
		if key_exists:
			bucket[i] = ((key,value))
		else:
			bucket.append((key,value))

	def retrieve(self, key):
		hash_key = hash(key) % len(self.hashmap)
		bucket = self.hashmap[hash_key]
		for i, kv in enumerate(bucket):
			k, v = kv
			return v
		raise KeyError

	def print(self):
		count = 0
		for bucket in self.hashmap:
			print(f"Bucket {count}: {bucket}")
			count += 1



map = HashMap()
map.insert('0494224654', 'Ludovico')
map.insert('0494508692', 'Caner')
map.insert('0494528034', 'Alex')
print(map.retrieve('0491639857'))
map.print()
print(hash((9573587, 'Caner', 'BXL')))
