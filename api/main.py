from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    # Run the app with auto-reload enabled (for development)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
