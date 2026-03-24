from fastapi import FastAPI, Path
from routes.documentRoutes import documentRouter

app = FastAPI()
app.include_router(documentRouter)