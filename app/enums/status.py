# Python
from enum import Enum


class Status(Enum):
    # comprando: str = "comprando"
    # comprado: str = "comprado"
    pre_venta: str = "pre_venta"
    en_venta: str = "en_venta"
    vendido: str = "vendido"
