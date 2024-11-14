from fastapi import APIRouter
from Aplicattion.Faturas.FaturaApp import FaturaApp
from fastapi import HTTPException

class FaturaController:
   router = APIRouter(prefix="/faturas")

   @router.get("/{mes}/{ano}", tags=["Faturas"], summary="Retorna as faturas dos cartões de um determinado mês/ano")
   def RetornarFaturasCartaoMesCorrespondente(mes: int, ano: int ):
    faturasRetornadas = FaturaApp.RetornaFaturasCartaoMes(mes, ano)

    if faturasRetornadas:
       return faturasRetornadas
    else:
      raise HTTPException(status_code=404, detail="Faturas não encontradas") 

    