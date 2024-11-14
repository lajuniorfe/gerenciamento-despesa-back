from datetime import date, datetime
from fastapi import APIRouter
from fastapi import HTTPException
from Aplicattion.Despesas.DespesaApp import DespesaApp 

class DespesaController():
    router = APIRouter(prefix="/despesas")

    @router.get("/{mes}/{ano}", tags=["Despesas"], summary="Retorna despesas do mês/ano")
    def RetornoDespesas(mes: int, ano: int):
        despesasRetornadas = DespesaApp.RetornarDespesasMes(mes, ano)

        if despesasRetornadas:
            return despesasRetornadas
        else:
            raise HTTPException(status_code=404, detail="Despesas não encontradas") 
        
    
    @router.get("/grafico-categoria", tags=["Despesas"], summary="Retorna dados gráficos de despesas por categorias")
    def RetornoDadosGraficoDespesaCategorias(data: date):
        dados = DespesaApp.RetornarDadosGraficoDespesaCategoria(data)

        if dados:
            return dados
        else:
            raise HTTPException(status_code=404, detail="Dados para gráficos não retornados.")
