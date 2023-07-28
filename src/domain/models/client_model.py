from dataclasses import dataclass


@dataclass
class ClientModel:
    client_id: str
    name: str
    email: str
    address: str
