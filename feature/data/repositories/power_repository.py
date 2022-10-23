from typing import Tuple

from core.errors.exceptions import InvalidValueException
from core.errors.failure import Failure, InvalidValuesFailure
from feature.data.datasource.power_datasource import PowerDataSource
from feature.data.models.power_model import PowerModel
from feature.domain.entities.power_entity import PowerEntity
from feature.domain.repositories.power_repository_interface import PowerRepositoryInterface


class PowerRepository(PowerRepositoryInterface):
    powerDataSource: PowerDataSource

    def get_power(self, nums: Tuple[int, int]) -> PowerEntity | Failure:
        try:
            power: PowerModel = self.powerDataSource.get_power()
            return power
        except InvalidValueException:
            return InvalidValuesFailure()

    def __init__(self, power_data_source: PowerDataSource):
        self.powerDataSource = power_data_source
