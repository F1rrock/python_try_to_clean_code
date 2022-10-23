from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from core.errors.failure import Failure

Type = TypeVar("Type")
Params = TypeVar("Params")


@dataclass
class UseCase(ABC, Generic[Type, Params]):
    @abstractmethod
    def __call__(self, nums: Params) -> Type | Failure:
        pass
