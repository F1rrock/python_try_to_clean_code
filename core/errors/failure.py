from abc import ABC


class Failure(ABC):
    pass


class InvalidValuesFailure(Failure):
    pass


class IncorrectArgumentsFailure(Failure):
    pass
