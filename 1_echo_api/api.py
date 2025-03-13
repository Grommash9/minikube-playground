from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(docs_url="/")

class EchoData(BaseModel):
    data: str

@app.post("/echo")
async def echo(data: EchoData):
    return {"data": data.data}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)