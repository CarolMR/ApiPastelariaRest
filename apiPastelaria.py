from fastapi import FastAPI
from settings import HOST, PORT, RELOAD

from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO

app = FastAPI()

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

# cria, caso não existam, as tabelas de todos os modelos importados
import db
db.criaTabelas()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)