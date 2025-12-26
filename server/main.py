from fastapi import FastAPI
from servermodule1.router import router as auth_router
from servermodule2.router import router as pricing_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(pricing_router)
