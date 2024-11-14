import datetime
from typing import Dict, List
from Infra.Despesas.DespesaRepository import DespesaRepository
import json


class DespesaApp:
    def RetornarDespesasMes(mes: int, ano: int) -> List[Dict]:
        despesasRetornadas = DespesaRepository.BuscarDespesaPorData(mes, ano)

        if isinstance(despesasRetornadas, str):
            despesasRetornadas =  json.loads(despesasRetornadas)

        return despesasRetornadas
    
    def RetornarDadosGraficoDespesaCategoria(data: datetime ) -> List[Dict]:
        dados = DespesaRepository.RetornarDadosGraficosDespesaPorCategoria(data)

        if isinstance(dados, str):
           dados = json.loads(dados)

        return dados