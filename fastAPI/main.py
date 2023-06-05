from fastapi import FastAPI
import random

app = FastAPI()

array_conselhos = [
"Fazer o makefile no começo",
"Criar os próprios testes",
"Refatorar códigos",
"Incrementar o contador na linha da condição",
"Se for bolsista não faça o bônus",
"Compile com -g pra usar o debugger",
"Debugar enquanto está fazendo o codigo"
]

# valor_aleatorio = random.choice(array_conselhos)

@app.get("/")
async def root():
    return {random.choice(array_conselhos)}