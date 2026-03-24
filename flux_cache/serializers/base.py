from abc import ABC, abstractmethod
from typing import Any


class BaseSerializer(ABC):


	@abstractmethod
	def dumps(self, value: Any) -> bytes:
		pass

	@abstractmethod
	def loads(self, data: bytes) -> Any:
		pass
