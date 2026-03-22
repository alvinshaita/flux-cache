from flux_cache.backends.base import BaseBackend


class MemoryBackend(BaseBackend):
	def __init__(self):
		self.store = {}

	def has(self, key):
		# print("999", key in self.store)
		return key in self.store

	def get(self, key):
		return self.store.get(key)

	def set(self, key, value):
		# print("888", key, value)
		self.store[key] = value

	def delete(self, key):
		self.store.pop(key, None)

	def clear(self):
		self.store.clear()
