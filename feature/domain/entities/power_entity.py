from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class PowerEntity:
    base: int
    extent: int

    @abstractmethod
    def __init__(self, base: int, extent: int):
        self.base = base
        self.extent = extent
