from fastapi import FastAPI 
from Api.Despesas.DespesaController import DespesaController
from Api.Faturas.FaturaController import FaturaController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(DespesaController.router)
app.include_router(FaturaController.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

