import json
from typing import Any

from .base import BaseSerializer


class JsonSerializer(BaseSerializer):

	def dumps(self, value: Any) -> bytes:
		return json.dumps(value)

	def loads(self, data: bytes) -> Any:
		return json.loads(data)
