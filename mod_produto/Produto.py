from pydantic import BaseModel

class Produto(BaseModel):
    id_Produto: int = None
    nome: str
    descricao: str = None
    foto: bytes
    valor_unitario: float = None
