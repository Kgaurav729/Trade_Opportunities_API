from fastapi import FastAPI
from routes.analyze import router as analyze_router
from routes.auth import router as auth_router

app = FastAPI(title="Trade Opportunities API")


app.include_router(analyze_router, prefix="/analyze", tags=["Analysis"])
app.include_router(auth_router,tags=["Auth"])
