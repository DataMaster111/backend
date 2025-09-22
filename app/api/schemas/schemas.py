from pydantic import BaseModel


class DBRequest(BaseModel):
    db_type: str
    host: str
    port: int
    database: str
    username: str
    password: str