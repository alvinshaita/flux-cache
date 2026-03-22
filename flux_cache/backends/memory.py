from flux_cache.backends.base import BaseBackend
from typing import Any, Optional


class MemoryBackend(BaseBackend):
	def __init__(self):
		self.store = {}

	def has(self, key: str) -> bool:
		return key in self.store

	def get(self, key: str) -> Optional[Any]:
		return self.store.get(key)

	def set(self, key: str, value: Any) -> None:
		self.store[key] = value

	def delete(self, key: str) -> None:
		self.store.pop(key, None)

	def clear(self) -> None:
		self.store.clear()
