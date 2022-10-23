from dataclasses import dataclass

from core.errors.failure import Failure, InvalidValuesFailure, IncorrectArgumentsFailure
from feature.domain.use_cases.power import Power


@dataclass
class PowerBusinessLogic:
    powerNums: Power

    @staticmethod
    def get_from_inputs(input1: str, input2: str) -> tuple:
        return input1, input2

    def get_power(self, input1: str, input2: str) -> str:
        failure_or_power: int | Failure = self.powerNums(self.get_from_inputs(input1, input2))
        if type(failure_or_power) is Failure:
            if failure_or_power is InvalidValuesFailure:
                return 'invalid value'
            elif failure_or_power is IncorrectArgumentsFailure:
                return 'invalid value'
            else:
                return 'unhandled failure'
        return str(failure_or_power)

    def __init__(self, power_nums: Power):
        self.powerNums = power_nums
