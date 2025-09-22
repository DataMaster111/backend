"""Файл для создания коннекта отдельно к PostgreSQL и ClackHouse"""
import psycopg2
from .base_connector import BaseConnector


class PostgresConnector(BaseConnector):
    def connect(self):
        try:
            connect = psycopg2.connect(**self.connector_params)
            return True
        except Exception as e:
            raise {"Error connection Postgres": {e}}

    def disconnect(self):
        ...

    def get_schema(self):
        ...

    def get_sample_data(self):
        ...