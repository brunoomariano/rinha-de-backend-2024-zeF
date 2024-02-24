from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class TransactionDTO(BaseModel):
    valor: int
    tipo: str
    descricao: str


class BalanceDTO(BaseModel):
    saldo: int = Field(alias="saldo")
    limite: int = Field(alias="limite")
    data_extrato: datetime = Field(default_factory=datetime.now)


class ExtractDTO(BaseModel):
    saldo: BalanceDTO
    ultimas_transacoes: List[TransactionDTO]
