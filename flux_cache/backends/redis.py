import json
import redis
import threading
import time
from typing import Any, Optional

from .base import BaseBackend


class RedisBackend(BaseBackend):
	def __init__(self, url="redis://localhost:6379/0", prefix="flux-cache"):
		self.prefix = prefix
		self.red = redis.Redis.from_url(url)

	def _serialize(self, value: Any) -> bytes:
		return json.dumps(value)

	def _deserialize(self, value: Optional[bytes]) -> Any:
		if value is None:
			return None

		try:
			return json.loads(value)
		except:
			return value

	def _key(self, key: str) -> str:
		return f"{self.prefix}:{key}"

	def has(self, key: str) -> bool:
		namespaced_key = self._key(key)
		present = self.red.exists(namespaced_key)
		return True if present == 1 else False

	def get(self, key: str) -> Optional[Any]:
		namespaced_key = self._key(key)
		value = self.red.get(namespaced_key)
		if value is None:
			return None

		deserialized_value = self._deserialize(value)
		return deserialized_value, None

	def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
		serialized_value = self._serialize(value)
		namespaced_key = self._key(key)
		self.red.set(namespaced_key, serialized_value, ex=ttl)

	def delete(self, key: str) -> None:
		namespaced_key = self._key(key)
		self.red.delete(namespaced_key)

	def clear(self) -> None:
		keys = self.red.keys(f"{self.prefix}*")
		if keys:
			self.red.delete(*keys)
