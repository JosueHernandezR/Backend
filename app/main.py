from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

from app.api.api_v1.api import api_router
from app.core.config import settings

import time

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers['X-Process-Time'] = str(process_time)

#     return response

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@app.get("/app/info", tags=["App"])
async def app_info(setting: settings):
    return {
        "app_name"      : settings.APP_NAME,
        "app_version"   : settings.APP_VERSION,
        "app_framework" : settings.APP_FRAMEWORK,
        "app_date"      : settings.APP_DATE,
    }

@app.get("/health")
def health():
    return {"message": "ok!"}

app.include_router(api_router, prefix=settings.API_V1_STR)