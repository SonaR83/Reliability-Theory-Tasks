from fastapi import APIRouter

root = APIRouter()


@root.get("/")
async def read_root() -> dict:
    return {"service": "reliability theory backend"}
