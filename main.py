from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello"}

@app.get("/{id}")
def read_root(id:int = Path(..., description="Something")):
    return {id}