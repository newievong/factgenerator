from fastapi import FastAPI
from pydantic import BaseModel

class Facts(BaseModel):
    id: int
    fact: str

app = FastAPI()

facts_db = [Facts(id=0, fact="Pad Thai was a dish that was originally created"
                              "to boost Thailand's tourism."),
            Facts(id=1, fact="Massman Curry was a dish that was"
                              "heavily influenced by Muslim culture."),
            Facts(id=2, fact="Silphium is an "
                              "ancient herb that the Greeks and Romans used and is completely extinct in"
                              "modern times."),
            Facts(id=3, fact="All Spanish/Spanish colonized countries have a"
                              "form of lechon, or roasted pig."),
            Facts(id=4, fact='India grows the most spices internationally, growing about 76% of the global spices.')]

@app.get("/")
async def get_all():
    return facts_db

@app.get("/fact/{id}")
async def get_by_id(id: int):
    return facts_db[id]

@app.post('/fact')
async def add(fact: str):
    newfact = Facts(id=len(facts_db), fact = fact)
    facts_db.append(newfact)
    return newfact