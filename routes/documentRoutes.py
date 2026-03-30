from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.documentServices import document_upload_service


documentRouter = APIRouter()

@documentRouter.post("/document")
async def document_upload(req: Request):
    headers = req.headers
    body = await req.body()
    print(headers)

    print(body.decode())

    return document_upload_service()