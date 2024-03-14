import aiofiles
import json


from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from fastapi import status

request_task = APIRouter()


@request_task.get("/request_task/{task}")
async def task_request(task: str) -> ORJSONResponse:

    try:
        async with aiofiles.open(f"tasks/bunch/{task}.json") as json_file:
            raw_data = await json_file.read()
            data = json.loads(raw_data)
        content = {"content": f"{json.dumps(data)}"}
        return ORJSONResponse(content=content, status_code=status.HTTP_200_OK)

    except FileNotFoundError:
        return ORJSONResponse(content="file not found",
                              status_code=status.HTTP_404_NOT_FOUND)
