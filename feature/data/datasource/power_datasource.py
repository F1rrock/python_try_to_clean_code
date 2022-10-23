from abc import ABC, abstractmethod
from dataclasses import dataclass

from overrides import overrides

from core.errors.exceptions import InvalidValueException, IncorrectArgumentsException
from feature.data.models.power_model import PowerModel


@dataclass
class PowerDataSourceInterface(ABC):
    @abstractmethod
    def get_power(self, nums) -> PowerModel:
        pass


@dataclass
class PowerDataSource(PowerDataSourceInterface):
    @overrides(PowerDataSourceInterface)
    def get_power(self, nums) -> PowerModel:
        if not type(nums) is tuple or len(nums) != 2:
            raise IncorrectArgumentsException
        try:
            nums[0:] = int(nums[0])
            nums[1:] = int(nums[1])
            return PowerModel.from_tuple(nums=nums)
        except InvalidValueException:
            raise InvalidValueException
