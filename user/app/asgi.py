from typing import Callable
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .config.base import Base
from .config.logger import log_request, logger
from .config.postgres import Postgres
from time import perf_counter
from .routers import router

logger.info(f'Environment: {Base.name.title()} [{Base.env.upper()}]')
logger.info(f'PostgreSQL : {Postgres().url}')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = Base.origins,
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["GET","POST","PUT"]
)


@app.middleware("http")
async def request_logger(request: Request, callback: Callable):
    start = perf_counter()
    response = await callback(request)
    processing_time = perf_counter() - start
    await log_request(request, response.status_code, processing_time)
    return response


@app.get('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

app.include_router(router)
