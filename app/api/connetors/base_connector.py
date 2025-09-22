from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseConnector(ABC):

    def __init__(self, connector_params: Dict[str: Any]):
        self.connector_params = connector_params

    @abstractmethod
    def connect(self):
        """Устанавливаем соединение"""
        pass

    @abstractmethod
    def disconnect(self):
        """Отключаемся от бд"""
        pass

    @abstractmethod
    def get_schema(self):
        """Возвращаем таблицы из бд"""
        pass

    @abstractmethod
    def get_sample_data(self):
        """Проверяем данные из бд"""
        pass
