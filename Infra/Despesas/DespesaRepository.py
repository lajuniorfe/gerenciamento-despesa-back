
from datetime import datetime
from sqlalchemy import text
from Infra.Data.database import engine
import pandas as pd
import json

class DespesaRepository:
    def BuscarDespesaPorData(mes: int, ano: int) -> str:
        query = text("""SELECT d.descricao, 
                     CASE WHEN tp.id = 2 THEN cc.nome
                     ELSE tp.nome END AS pagamento,
                     d.valor, d.data_despesa AS data, c.nome AS categoria, COUNT(p.numero_parcela) AS parcelas 
                     FROM despesa d 
                     LEFT JOIN categoria c ON c.id = d.id_categoria
                     LEFT JOIN parcela p ON p.id_jurema = d.id
                     LEFT JOIN fatura f ON f.id = p.id_fatura
                     LEFT JOIN cartao cc ON cc.id = f.id_cartao
                     LEFT JOIN transacao_despesa td ON td.id_despesa = d.id
                     LEFT JOIN tipo_pagamento tp ON tp.id = td.id_tipopagamento
                     WHERE EXTRACT(MONTH FROM d.data_despesa) = :mes AND EXTRACT(YEAR FROM d.data_despesa) = :ano
                     GROUP BY d.descricao, pagamento, d.valor, d.data_despesa, c.nome""")

        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection, params={"mes": mes, "ano": ano})
        
        json_result = df.to_json(orient="records", date_format="iso")
        formataJson = json.loads(json_result)
        jsonFormatado = json.dumps(formataJson, indent=4)

        return jsonFormatado
    
    def RetornarDadosGraficosDespesaPorCategoria(data: datetime) -> str:
        query = text("""select d.descricao, d.valor, c.nome as categoria from despesa d
        left join categoria c on d.id_categoria = c.id""")

        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection, params={"mes": data.month, "ano": data.year})

        category_summary = df.groupby("categoria")["valor"].sum()
        data_for_chart = {
            "labels": list(category_summary.index),
            "values": list(category_summary.values)
        }

        json_result = json.dumps(data_for_chart, indent=4)
        return json_result