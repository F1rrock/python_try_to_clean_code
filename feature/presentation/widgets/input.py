from tkinter import Tk

from overrides import overrides

from feature.presentation.widgets.widget import Widget


class Input(Widget):
    @overrides(Widget)
    def __init__(self, root: Tk):
        super().__init__(root)
