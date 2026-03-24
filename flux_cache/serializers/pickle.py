import pickle
from typing import Any

from .base import BaseSerializer


class PickleSerializer(BaseSerializer):

	def dumps(self, value: Any) -> bytes:
		return pickle.dumps(value)

	def loads(self, data: bytes) -> Any:
		return pickle.loads(data)
