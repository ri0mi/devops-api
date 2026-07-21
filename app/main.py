from fastapi import FastAPI

app = FastAPI(title="DevOps API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "DevOps API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sum/{a}/{b}")
def sum_numbers(a: int, b: int):
    return {"result": a + b}
