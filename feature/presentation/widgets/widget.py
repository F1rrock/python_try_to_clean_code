from abc import ABC, abstractmethod
from dataclasses import dataclass
from tkinter import Tk


@dataclass
class Widget(ABC):
    root: Tk
    column: int = 0

    @abstractmethod
    def __init__(self, root: Tk):
        self.root = root

    def __init_subclass__(cls):
        cls.column += 1
