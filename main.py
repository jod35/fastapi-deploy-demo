from fastapi import FastAPI



app = FastAPI(
    title="Bookly",
    description="A REST API for a book review service",
    version="v1",
    docs_url="/docs"
)

@app.get('/')
async def hello():
    return {"message":"Hello World"}
