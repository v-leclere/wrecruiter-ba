from fastapi import FastAPI
from pydantic import BaseModel

from app.rpn.calculator import Calculator


class Expression(BaseModel):
    expression: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/compute/")
async def exec_expression(expression: Expression):
    calculator = Calculator()
    return { "result": calculator.resolve(expression.expression)}
