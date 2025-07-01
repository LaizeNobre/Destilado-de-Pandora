import uuid
from datetime import datetime


class BaseEntity:
    def __init__(self):
        self.id = self._gerar_id()
        self.data_criacao = datetime.now()

    def __eq__(self,other):
        return isinstance(other, self.__class__) and self.id == other.id
 
    def _gerar_id(self):
        return uuid.uuid4()
    

class Produto(BaseEntity):
    pass

class Funcionario(BaseEntity):
    pass

class Cliente(BaseEntity):
    pass

class Venda(BaseEntity):
    pass