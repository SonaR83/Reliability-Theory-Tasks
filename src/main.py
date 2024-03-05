from fastapi import FastAPI

from api.v1.router.part_1 import p1t1
from api.v1.router.root import root

app = FastAPI()
app.include_router(router=root, tags=['root'])
app.include_router(router=p1t1,  tags=['part 1'])