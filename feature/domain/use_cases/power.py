from overrides import overrides

from core.errors.failure import Failure
from core.use_cases.use_case import UseCase
from dataclasses import dataclass

from feature.domain.entities.power_entity import PowerEntity
from feature.domain.repositories.power_repository_interface import PowerRepositoryInterface


@dataclass
class Power(UseCase[int, tuple]):
    powerRepository: PowerRepositoryInterface

    @overrides(UseCase)
    def __call__(self, nums: tuple) -> int | Failure:
        power_or_failure: PowerEntity | Failure = self.powerRepository.get_power(nums=nums)
        if type(power_or_failure) is Failure:
            return power_or_failure
        root: int = 1
        for i in range(power_or_failure.extent):
            root *= power_or_failure.base
        return root
