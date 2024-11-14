from typing import Dict, List
from Infra.Faturas.FaturaRepository import FaturaRepository

class FaturaApp:
   
    def RetornaFaturasCartaoMes(mes: int, ano: int) -> List[Dict]:
       retornoFaturas = FaturaRepository.BuscarFaturasCartaoPorData(mes, ano)

       if isinstance(retornoFaturas, str):
        import json
        retornoFaturas = json.loads(retornoFaturas)  

       for fatura in retornoFaturas:
          if "valor" in fatura:
             fatura["valor"] = round(fatura["valor"], 2) 
    
       return retornoFaturas