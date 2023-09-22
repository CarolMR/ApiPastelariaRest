from fastapi import APIRouter
from mod_produto.Produto import Produto

# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

#@router.get("/produto/", tags=["Produto"])
#def get_produto():
#    return {"msg": "get todos executado"}, 200

#@router.get("/produto/{id}", tags=["Produto"])
#def get_produto(id: int):
#    return {"msg": "get um executado"}, 200

#@router.post("/produto/", tags=["Produto"])
#def post_produto(p: Produto):
#    return {"msg": "post executado", "nome": p.nome, "cpf": p.cpf, "telefone": p.telefone}, 200

#@router.put("/produto/{id}", tags=["Produto"])
#def put_produto(id: int, p: Produto):
#    return {"msg": "put executado", "id": id, "nome": p.nome, "cpf": p.cpf, "telefone": p.telefone}, 201

#@router.delete("/produto/{id}", tags=["Produto"])
#def delete_produto(id: int):
#    return {"msg": "delete executado"}, 201

@router.get("/produto/", tags=["Produto"])  #feito no 21/09
def get_produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:    
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(p: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(None, p.nome, p.descricao, p.foto, p.valor_unitario)
        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).one()
        
        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()       

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:

        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close() 
