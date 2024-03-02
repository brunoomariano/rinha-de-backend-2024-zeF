from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Cliente, Transacao
from config.db_config import get_session
from dto.dto import ExtractDTO, TransactionDTO
from sqlalchemy.exc import NoResultFound


app = FastAPI()


@app.post('/clientes/{id}/transacoes', status_code=200)
def transaction(id: int, req: TransactionDTO,
                db: Session = Depends(get_session)):

    client = db.query(Cliente).where(Cliente.id == id).one()

    if (not client):
        raise HTTPException(status_code=404, detail="Id not found")

    if (req.tipo == "d" or req.tipo == "c"):
        if (req.tipo == "d"):
            if (req.valor > client.limite):
                raise HTTPException(status_code=422,
                                    detail="Insufficient funds")

            transaction = Transacao(
                valor=req.valor,
                tipo=req.tipo,
                descricao=req.descricao,

                client_id=client.id
            )
            db.add(transaction)
            client.saldo -= req.valor
            db.commit()

            return {'limite': client.limite,
                    'saldo': client.saldo}

    raise HTTPException(status_code=422, detail="Field 'tipo' is invalid")


@app.get('/clientes/{id}/extrato', status_code=200, response_model=ExtractDTO)
def extrato(id: int, db: Session = Depends(get_session)):
    try:
        client = db.query(Cliente).where(Cliente.id == id).one()
        transactions = db.query(Transacao)\
            .where(Transacao.client_id == id).all()

        return {"saldo": client, "ultimas_transacoes": transactions}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="client not found")
