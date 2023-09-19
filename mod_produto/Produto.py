from pydantic import BaseModel

class Produto(BaseModel):
    id_Produto: int = None
    nome: str
    descrição: str = None
    foto: bytes
    valor_unitario: float = None