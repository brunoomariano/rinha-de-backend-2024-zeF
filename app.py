from fastapi import FastAPI, HTTPException, Depends
from typing import Dict, Union
from sqlalchemy.orm import Session
from db_models import Cliente, Transacao
from db_config import get_session
from dto import ExtractDTO
from sqlalchemy.exc import NoResultFound


app = FastAPI()


@app.post('/clientes/{id}/transacoes', status_code=200)
def transaction(id: int, req: Dict[str, Union[int, str]]):
    pass


@app.get(
    '/clientes/{id_cliente}/extrato',
    status_code=200,
    response_model=ExtractDTO)
def extrato(id_cliente: int, db: Session = Depends(get_session)):
    try:
        client = db.query(Cliente).filter_by(id=id_cliente).one()
        transactions = db.query(Transacao)\
            .filter_by(client_id=id_cliente).all()

        return {"saldo": client, "ultimas_transacoes": transactions}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="client not found")
