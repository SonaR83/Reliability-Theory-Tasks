from fastapi import FastAPI

from api.v1.router.root import root
from api.v1.router.part_1 import part_1
from api.v1.router.part_2 import part_2
from api.v1.router.request_task import request_task
from middleware.cors import configure_cors

app = FastAPI()
configure_cors(app)
app.include_router(router=root, tags=['root'])
app.include_router(router=request_task, tags=['request_task'])
app.include_router(router=part_1, tags=['part 1'])
app.include_router(router=part_2, tags=['part 2'])
