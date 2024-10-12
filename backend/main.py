from fastapi import FastAPI

app = FastAPI()

@app.get("/{region_id}/{year}")
async def read_root():
    return {"message": "Hello, World!"}
