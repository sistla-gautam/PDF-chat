# This document will be for the different routes on the document


from fastapi import APIRouter


documentRouter = APIRouter()

@documentRouter.post("/document")
def document_upload():
    return {"document":"uploaded"}