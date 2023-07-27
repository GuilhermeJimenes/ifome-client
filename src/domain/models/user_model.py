from dataclasses import dataclass


@dataclass
class UserModel:
    client_id: str
    name: str
    email: str
    address: str
