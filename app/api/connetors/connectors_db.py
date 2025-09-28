"""Файл для создания коннекта отдельно к PostgreSQL и ClackHouse. На будущее"""
import psycopg2
from .base_connector import BaseConnector


class PostgresConnector(BaseConnector):
    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            return True
        except Exception as e:
            raise {"Error connection Postgres": {e}}

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def get_schema(self):
        cursor = self.connection.cursor()


    def get_sample_data(self):
        ...