class Despesa:
    Descricao: str
    Valor: float
    Data: str
    
    def __init__(self, descricao: str, valor: float, data: str):
        self.Descricao = descricao
        self.Valor = valor
        self.Data = data 