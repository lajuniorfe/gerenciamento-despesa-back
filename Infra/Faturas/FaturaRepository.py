import pandas as pd
from sqlalchemy import text
from Infra.Data.database import engine
import json

class FaturaRepository:

    def BuscarFaturasCartaoPorData(mes: int, ano: int) -> str:

        query = text(""" SELECT C.nome, F.valor, F.data_vencimento, F.id_cartao, F.status_pagamento as status FROM FATURA F
                     LEFT JOIN CARTAO C ON C.ID = F.ID_CARTAO
                     WHERE EXTRACT(MONTH FROM F.mes_correspondente) = :mes 
                     AND EXTRACT(YEAR FROM F.mes_correspondente) = :ano
                     """)
        
        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection, params={"mes": mes, "ano": ano})

        json_result = df.to_json(orient="records", date_format="iso")
        formataJson = json.loads(json_result)
        jsonFormatado = json.dumps(formataJson, indent=4)

        return jsonFormatado
