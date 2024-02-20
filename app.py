from fastapi import FastAPI, HTTPException
from list import clientes
from typing import Dict, Union


app = FastAPI()


@app.post('/clientes/{id}/transacoes', status_code=200)
def transaction(id: int, req: Dict[str, Union[int, str]]):
    
    client = next((c for c in clientes if c['id'] == id), None)
    
    if client:
        if(req['tipo'] == 'c'):
            client['saldo'] -= req['valor']
            return {
                'limite': client['limite'],
                'saldo': client['saldo']
            }
            
        elif(req['tipo'] == 'd'):
            if(req['valor'] <= client['limite']):
                client['saldo'] -= req['valor']
                return {
                    'limite': client['limite'],
                    'saldo': client['saldo']
                }
            
        raise HTTPException(status_code=422, detail='incosistent value')
           


    raise HTTPException(status_code=404, detail='client not found')


@app.get('/clientes/{id}/extrato')
def extrato():
    
    
    return {'msg': 'this is my first test'}


