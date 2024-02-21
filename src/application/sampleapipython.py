# sampleapipython:

from fastapi import FastAPI

app: FastAPI = FastAPI(
    title="Sample API Python",
    description="USBTCA202402"
)

@app.get("/sampleAPIPython",
    summary="Sample API Python"

    tags=["SampleAPIPython"])
async def operacion_get(dato_entrada: str):
    return