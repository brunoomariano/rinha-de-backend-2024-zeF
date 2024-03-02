from sqlalchemy import (
    Column, Integer, String,
    BigInteger, CHAR, ForeignKey,
    Text, TIMESTAMP, func
    )
from config.db_config import Base


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    limite = Column(BigInteger)
    saldo = Column(BigInteger)


class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True)
    valor = Column(BigInteger)
    tipo = Column(CHAR(1))
    descricao = Column(Text)
    data_criacao = Column(TIMESTAMP, default=func.now())

    client_id = Column(Integer, ForeignKey('clientes.id'))
