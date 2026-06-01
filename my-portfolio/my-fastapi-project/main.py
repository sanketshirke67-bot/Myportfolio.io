from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI on Fedora!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}