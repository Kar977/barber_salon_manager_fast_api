from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
MICROSERVICE_URL = "http://localhost:8001"

@app.get("/home")
async def get_home_from_microservice():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{MICROSERVICE_URL}/home")
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=500, detail=str(exc))
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
